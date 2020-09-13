package com.web.tuopu;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;


public class SocketPy extends Thread {

    //����һ��Socket����
    Socket socket = null;

    public SocketPy(String host, int port) {
        try {
            //��Ҫ��������IP��ַ�Ͷ˿ںţ����ܻ����ȷ��Socket����
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
    	
        //�ͻ���һ���ӾͿ���д���ݸ���������
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

    //��Socket����д���ݣ���Ҫ�¿�һ���߳�
    class sendMessThread extends Thread{
    	
    	
        @Override
        public void run() {
            super.run();
            //д����
           
            OutputStream os= null;
            try {
                os= socket.getOutputStream();
                os.write((command).getBytes());
                os.flush();
                try {
                    // ��Sock���������
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
    

    
//    //�������
//    public static void main(String[] args) {
//        //��Ҫ����������ȷ��IP��ַ�Ͷ˿ں�
//    	Long t1 = System.currentTimeMillis();
//    	SocketPy clientTest=new SocketPy("127.0.0.1", 50007);
//        System.out.println(clientTest.execCommand("1./test/1.csv|0"));
//        System.out.println(System.currentTimeMillis()-t1);
//    }
}
