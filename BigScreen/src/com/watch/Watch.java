package com.watch;

import com.util.file.FileHandle;
import com.web.tuopu.Config;
import com.web.tuopu.DataServlet;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
public class Watch {

	static final String FoldPath=Config.checkdir;
	static FileHandle fh=new FileHandle();

	
	
	static String prefile="";
	static String prehandle="";
	static WatchService service;
	static Path path;
	static WatchKey watchKey;
	public static void init(String Foldpath)
	{
		try {
			service = FileSystems.getDefault().newWatchService();
			path=Paths.get(Foldpath);
			path.register(service, StandardWatchEventKinds.ENTRY_CREATE,StandardWatchEventKinds.ENTRY_DELETE,StandardWatchEventKinds.ENTRY_MODIFY);
			watchKey=service.take();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public static void MONITOR(String Foldpath)
	{
		try{
			
			if(watchKey.reset()){
				if(Check_watch.exit)
					return;
				//获取一个watch key
				watchKey=service.take();
				for(WatchEvent<?> event:watchKey.pollEvents()){
					//如果时间列表不为空，打印事件内容
					WatchEvent.Kind<?> kind=event.kind();
					Path eventPath=(Path)event.context();
					String Str_kind=kind.toString();
					String Str_value="";
					switch(Str_kind){
					case "ENTRY_MODIFY" :
						Str_value="修改";
						break; //可选
					case "ENTRY_DELETE" :
						Str_value="删除";
						break; //可选
					case "ENTRY_CREATE" :
						Str_value="创建";
						break; //可选
					}
					String filename=eventPath.toString();
					if(prefile.equals(filename)&&prehandle.equals(Str_value))
						continue;
					String time=new SimpleDateFormat("yyyy/MM/dd-HH:mm:ss:SSS").format(new Date()).toString();
					String info="时间："+time+" 文件：《"+filename+"》 操作：‘"+Str_value+"’";
					if(Str_value.equals("修改"))
					{
						DataServlet.haveCheckedRoot(Config.checkdir+"/"+filename,true,null);
						info +=" 已更新";
						System.out.println("已更新");
					}
					info +="\r\n";
					System.out.println(info);
					fh.outFile(info,Config.checklog ,true);
					prefile=filename;
					prehandle=Str_value;
				}
				System.out.println("目录内容发生改变");

			}
		}catch(Exception e){
			e.printStackTrace();

		}
	}

}
