package com.python;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;

import com.alibaba.fastjson.JSONObject;
import com.bean.UserBean;
import com.util.file.FileHandle;
import com.web.tuopu.Config;

public class Ppyrun_pre {
	static StringHandle sh =new StringHandle();
	static FileHandle fh =new FileHandle();
	static final String workspace=Config.workspace;
//	public static void main(String[] args) {
//		
//		System.out.println(GET_Value_json("./test/8.csv","node_87"));
//		System.out.println(get_nodeinfo("./test/8.csv","node_87"));
//	}
	
	public static JSONArray GET_Value_json(String path,String pointnode)
	{
		JSONArray array_data=new JSONArray();
			ArrayList<UserBean> UserBeans_pre=GET__pre_value(path,pointnode);
			for (UserBean n:UserBeans_pre)
			{
				JSONObject job_node = new JSONObject();
				job_node.put("name", n.getName_port().replaceAll("[\\[']", ""));
				job_node.put("sys", n.getName_sys().replaceAll("[\\[']", ""));
				job_node.put("color","rgba(0,255,0,0.93)");
				 array_data.put(job_node);
			}
			ArrayList<UserBean> UserBeans_be=GET__be_value(path,pointnode);
			for (UserBean n:UserBeans_be)
			{
				JSONObject job_node = new JSONObject();
				job_node.put("name", n.getName_port().replaceAll("[\\[']", ""));
				job_node.put("sys", n.getName_sys().replaceAll("[\\[']", ""));
				job_node.put("color","rgba(0,0,255,0.93)");
				 array_data.put(job_node);
			}
		
		return array_data;
	}
	
	
	public static ArrayList<UserBean> GET__pre_value(String filename,String pointnode)
	{
		System.out.println(filename+" "+pointnode);
		List<List<String>> result=com.web.tuopu.Ppyrun.get_nodeinfo(filename,pointnode);
		List<String> pre_name_nodes=result.get(0);
		List<String> pre_name_sys=result.get(1);
		ArrayList<UserBean> VALUE_BEAN=new ArrayList<UserBean>();
		int i=0;
		for(String pre_node:pre_name_nodes)
		{
			
			UserBean bean=new UserBean();
			bean.setName_port(pre_node);
			bean.setName_sys(pre_name_sys.get(i));
			VALUE_BEAN.add(bean);
			i=i+1;
		}

		return VALUE_BEAN;
	}
	public static ArrayList<UserBean> GET__be_value(String filename,String pointnode)
	{
		List<List<String>> result=com.web.tuopu.Ppyrun.get_nodeinfo(filename,pointnode);
		List<String> be_name_node=result.get(2);
		List<String> be_name_sys=result.get(3);
		ArrayList<UserBean> VALUE_BEAN=new ArrayList<UserBean>();
		int i=0;
		for(String be_node:be_name_node)
		{
		
			UserBean bean=new UserBean();
			bean.setName_port(be_node);
			bean.setName_sys(be_name_sys.get(i));
			VALUE_BEAN.add(bean);
			i=i+1;
		}

		return VALUE_BEAN;
	}
//	//List中 第0个数据是前驱节点 第1个数据是对应前驱系统号 第2个数据是后驱节点 第3个数据是后驱系统号 其值均为String
//		public static List<List<String>> get_nodeinfo(String csvfile,String pointnode)
//		{
//			String predict_result="";
//			Runtime proc;
//			proc = Runtime.getRuntime();
//			try {
//				Process result=proc.exec("python");
//				OutputStream output=result.getOutputStream();
//				runOutput(output,"import os");
//				runOutput(output,"os.chdir('"+workspace+"')");
//				runOutput(output,"import client");
//				runOutput(output,"print(client.cl_get_csv_nodesys(r'"+csvfile+"',r'"+pointnode+"'))");
//				System.out.println("print(client.cl_get_csv_nodesys(r'"+csvfile+"',r'"+pointnode+"'))");
//				runFinish(output);
//				InputStream input=result.getInputStream();
//				BufferedReader br = null;
//				List<List<String>> outputlist=null;
//				br = new BufferedReader(new InputStreamReader(input, "GB2312"));
//				String line = null;
//				while ((line = br.readLine()) != null) {
//					predict_result+=(line).replace("'", "")+"\r\n";
//				}
//				String []spilt_result=predict_result.split("\\], \\[");
//				spilt_result[0]=spilt_result[0].substring(1);
//				if(spilt_result[spilt_result.length-1].length()>=3)
//					spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-3);
//				else{
//					outputlist=new ArrayList<List<String>>();
//					//spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-1);
//				}
//				input.close();
//				result.waitFor();
//				if(outputlist==null)
//					outputlist=sh.StringSplitByExpToStringList(sh.StringNlistToStringList(spilt_result), ", ");
//				return outputlist;
//
//			} catch (IOException | InterruptedException e) {
//				// TODO 自动生成的 catch 块
//				e.printStackTrace();
//			}
//			return new ArrayList<List<String>>();
//		}
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
