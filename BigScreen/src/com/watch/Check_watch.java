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
			//判断是否被中断
	        if(Thread.currentThread().isInterrupted()){
	            //处理中断逻辑
	            break;
	        }
			 //判断是否被中断
			Watch.MONITOR(FoldPath);
		}
	}

}
