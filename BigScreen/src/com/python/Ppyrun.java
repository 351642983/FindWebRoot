package com.python;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;

import com.alibaba.fastjson.JSONObject;
import com.bean.UserBean;
import com.util.file.FileHandle;
import com.web.tuopu.Config;
public class Ppyrun {
	static StringHandle sh =new StringHandle();
	static FileHandle fh =new FileHandle();
	static final String workspace=Config.workspace;

//	public static void main(String args[])
//	{	
//		System.out.println("AAAA");
//		//JSONArray array_data=GET_waring_json();
//		JSONArray array_data=GET_file_json("./test/6.csv");
//		System.out.println(GET_NAME("./test/6.csv"));
//		System.out.println(array_data);
//		//MONITOR("E:\\\\pycharm\\\\WorkPlace\\\\FINAL_TUO\\test");
//	}
	
	public static JSONArray GET_waring_json(String path)
	{
		JSONArray array_data=new JSONArray();
		List<String> paths=fh.getFileList(path);
		for(String file :paths)
		{
			System.out.println(file);
			ArrayList<UserBean> UserBeans=GET_value(file);
			for (UserBean n:UserBeans)
			{
				JSONObject job_node = new JSONObject();
				job_node.put("id",n.getName_port());
				job_node.put("name", n.getName_port());
				job_node.put("sys", n.getName_sys());
				job_node.put("alarm",n.getInfo()+"    "+n.getIndex());
				 array_data.put(job_node);
			}
			
		}
		return array_data;
	}
	public static JSONArray GET_file_json(String path)
	{
		JSONArray array_data=new JSONArray();
			ArrayList<UserBean> UserBeans=GET_value(path);
			for (UserBean n:UserBeans)
			{
				JSONObject job_node = new JSONObject();
				job_node.put("id",n.getName_port());
				job_node.put("name", n.getName_port());
				job_node.put("sys", n.getName_sys());
				job_node.put("alarm",n.getInfo()+"    "+n.getIndex());
				 array_data.put(job_node);
			}
			
		
		return array_data;
	}
	 public static void MONITOR(String pathplace)
		{
			JSONArray array_data=GET_waring_json(pathplace);
			System.out.println(array_data);
			try{

			//创建一个监听服务
			WatchService service=FileSystems.getDefault().newWatchService();
			//设置路径
			Path path=Paths.get(pathplace);
			//注册监听器
			path.register(service, StandardWatchEventKinds.ENTRY_CREATE,StandardWatchEventKinds.ENTRY_DELETE,StandardWatchEventKinds.ENTRY_MODIFY);

			WatchKey watchKey;

			//使用dowhile
			do{
			//获取一个watch key
			watchKey=service.take();
			for(WatchEvent<?> event:watchKey.pollEvents()){
			//如果时间列表不为空，打印事件内容
			WatchEvent.Kind<?> kind=event.kind();
			Path eventPath=(Path)event.context();
			System.out.println(eventPath+":"+kind+":"+eventPath);

			}
			System.out.println("目录内容发生改变");
			array_data=GET_waring_json(pathplace);
			System.out.println(array_data);
			}while(watchKey.reset());
			}catch(Exception e){
			e.printStackTrace();

			}
		}
	 public static String GET_NAME(String filename)
	 {
		 List<List<String>> result=com.web.tuopu.Ppyrun.predict_csv(filename,0);
		String str="";
			int i=0;
			for(List<String> n:result)
			{
				if(i>0)
				{
					break;
				}
				str="node_"+n.get(1);
				i=i+1;
			}
			return str;
	 }
	public static ArrayList<UserBean> GET_value(String filename)
	{
		List<List<String>> result=com.web.tuopu.Ppyrun.predict_csv(filename,0);
		ArrayList<UserBean> VALUE_BEAN=new ArrayList<UserBean>();
		int i=0;
		for(List<String> n:result)
		{
			if(i>0)
			{
				break;
			}
			UserBean bean=new UserBean();
			bean.setName_sys("SYS_"+n.get(0));
			bean.setName_port("node_"+n.get(1));
			bean.setInfo(n.get(2));
			bean.setIndex(n.get(4));
			VALUE_BEAN.add(bean);
			i=i+1;
		}
		return VALUE_BEAN;
	}

//	//List中 第0个数据是系统号 第1个数据是主机号 第2个数据是警告信息 第3个数据是概率 其值均为String
//	public static List<List<String>> predict_csv(String filename)
//	{
//		String predict_result="";
//    	Runtime proc;
//		proc = Runtime.getRuntime();
//        try {
//			Process result=proc.exec("python");
//			OutputStream output=result.getOutputStream();
//			runOutput(output,"import os");
//			runOutput(output,"os.chdir(r'"+workspace+"')");
//			runOutput(output,"import client");
//			runOutput(output,"print(client.cl_predict_csv(r'"+filename+"'))");
//			System.out.println("print(client.cl_predict_csv(r'"+filename+"'))");
//			runFinish(output);
//			InputStream input=result.getInputStream();
//			BufferedReader br = null;
//			List<List<String>> outputlist=null;
//			br = new BufferedReader(new InputStreamReader(input, "GB2312"));
//			String line = null;
//			while ((line = br.readLine()) != null) {
//				predict_result+=line+"\r\n";
//			}
//			String []spilt_result=predict_result.split("\\], \\[");
//			spilt_result[0]=spilt_result[0].substring(1);
//			if(spilt_result[spilt_result.length-1].length()>=3)
//				spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-3);
//			else{
//				outputlist=new ArrayList<List<String>>();
//				//spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-1);
//			}
//			input.close();
//			result.waitFor();
//			if(outputlist==null)
//				outputlist=sh.StringSplitByExpToStringList(sh.StringNlistToStringList(spilt_result), ", ");
//			return outputlist;
//			
//		} catch (IOException | InterruptedException e) {
//			// TODO 自动生成的 catch 块
//			e.printStackTrace();
//		}
//        return new ArrayList<List<String>>();
//	}
	public static void runOutput(OutputStream outstream,String command)
	{
		try {
			outstream.write((command+"\r\n").getBytes());
		} catch (IOException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
	}
	public static void runFinish(OutputStream outstream)
	{
		try {
			outstream.flush();
			outstream.close();
		} catch (IOException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		
	}
}
