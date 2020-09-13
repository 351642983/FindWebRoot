package com.web.tuopu;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;


public class SocketPy extends Thread {

    //定义一个Socket对象
    Socket socket = null;

    public SocketPy(String host, int port) {
        try {
            //需要服务器的IP地址和端口号，才能获得正确的Socket对象
            socket = new Socket(host, port);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
    String result=null;
	public String command=null;
    @Override
    public void run() {
    	
        //客户端一连接就可以写数据给服务器了
        Thread t=new sendMessThread();
        t.start();
        try {
			t.join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        super.run();
    }
    
    public String execCommand(String cmd)
	{
    	command=cmd;
    	start();
    	try {
			join();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return result;
	}

    //往Socket里面写数据，需要新开一个线程
    class sendMessThread extends Thread{
    	
    	
        @Override
        public void run() {
            super.run();
            //写操作
           
            OutputStream os= null;
            try {
                os= socket.getOutputStream();
                os.write((command).getBytes());
                os.flush();
                try {
                    // 读Sock里面的数据
                    InputStream s = socket.getInputStream();
                    byte[] buf = new byte[1024];
                    int len = 0;
                    result="";
                    while ((len = s.read(buf)) != -1) {
                    	result+=new String(buf, 0, len,"UTF-8");
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
                
            } catch (IOException e) {
                e.printStackTrace();
            }
            
            try {
                os.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

    }
    

    
//    //函数入口
//    public static void main(String[] args) {
//        //需要服务器的正确的IP地址和端口号
//    	Long t1 = System.currentTimeMillis();
//    	SocketPy clientTest=new SocketPy("127.0.0.1", 50007);
//        System.out.println(clientTest.execCommand("1./test/1.csv|0"));
//        System.out.println(System.currentTimeMillis()-t1);
//    }
}
