package com.watch;

import com.web.tuopu.Config;
import com.web.tuopu.DataServlet;

public class Check_watch extends Thread {
	static final String FoldPath=Config.checkdir;
	public static volatile boolean exit = false; 
	
	@Override
	public void run() {
		Watch.init(FoldPath);
		while(!exit){
			//�ж��Ƿ��ж�
	        if(Thread.currentThread().isInterrupted()){
	            //�����ж��߼�
	            break;
	        }
			 //�ж��Ƿ��ж�
			Watch.MONITOR(FoldPath);
		}
	}

}
