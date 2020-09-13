package com.util;
import java.io.File;
import java.io.FileOutputStream;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.List;

import org.json.JSONArray;

import com.alibaba.fastjson.JSONObject;
import com.util.file.FileHandle;
import com.util.file.StringHandle;
import com.web.tuopu.Config;
public class GETlog {
	static FileHandle fh=new FileHandle();
	static StringHandle sh=new StringHandle();
public static void main(String[] args) {
	//Create_montior_json();
		JSONObject array_data=GETlog.Create_montior_json();
        
	System.out.println(array_data.toString());
}

static public JSONObject Create_montior_json()
{
	System.out.println("AAAAA");
	List<String> Values=fh.inputFile(Config.checklog);
	String pre="";
	System.out.println(pre);
	boolean isfold=true;
	List<JSONObject> array_data=new ArrayList<JSONObject>();

	
	for(String str:Values)
	{
	
		String time=sh.getExpStringAndRepalceEmpty("：(.*?) 文", str).get(0).replaceAll("[：文]", "");
		String time_hole=sh.getExpStringAndRepalceEmpty("\\d+/\\d+/\\d+-\\d+:\\d+", time).get(0);
		if(!time_hole.equals(pre))
		{
			pre=time_hole;
			isfold=true;
		}
		else
		{
			isfold=false;
		}
		String file=sh.getExpStringAndRepalceEmpty("《(.*?)》", str).get(0).replaceAll("[《》]", "");
		String Do=sh.getExpStringAndRepalceEmpty("‘(.*?)’", str).get(0).replaceAll("[‘’]", "");
		String info=sh.getExpStringAndRepalceEmpty("已更新", str).toString().replaceAll("[\\[\\]]", "");
		JSONObject job_pre = new JSONObject();
		if(isfold)
		{
			job_pre.put("time", pre);
			job_pre.put("file", " ");
			job_pre.put("Do", " ");
			job_pre.put("ptime", -1);
			array_data.add(job_pre);
		}
		JSONObject job = new JSONObject();
		job.put("time", time);
		job.put("file", file);
		job.put("Do", Do);
		job.put("info", info);
		job.put("ptime", pre);
		array_data.add(job);
		
	}
	JSONObject value_job = new JSONObject();
	value_job.put("code", 0);
	value_job.put("msg", "ok");
	value_job.put("data", array_data);
	value_job.put("count", 11);
	System.out.println(FileHandle.createJsonFile(value_job.toString(), Config.checklog_json, "data_montior"));
	return value_job;

}

static public JSONObject Create_root_json()
{
	List<String> Values=fh.inputFile(Config.monthdatadir+"\\rootlog.txt");
	String pre="";
	System.out.println(pre);
	
	boolean isfold=true;
	List<JSONObject> array_data=new ArrayList<JSONObject>();

	
	for(String str:Values)
	{

		String file=sh.getExpStringAndRepalceEmpty("E:(.*?)\\|", str).get(0).replaceAll("[\\|]", "");
		String sys=sh.getExpStringAndRepalceEmpty("\\|(.*?)\\|", str).get(0).replaceAll("[\\|]", "");
		String node=sh.getExpStringAndRepalceEmpty("\\|\\d+\\|'", str).get(0).replaceAll("[\\|']", "");
		String info=sh.getExpStringAndRepalceEmpty("\\|'(.*?)'\\|", str).get(0).replaceAll("[\\|']", "");
		String time=sh.getExpString("'\\|'(.*?)'\\|", str).get(0).replaceAll("[\\|']", "");
		String predit=sh.getExpStringAndRepalceEmpty("\\|0.\\d+", str).get(0).replaceAll("[\\|']", "");

		String time_hole=sh.getExpString("\\d+-\\d+-\\d+ \\d+:\\d+", time).get(0);
		if(!time_hole.equals(pre))
		{
			pre=time_hole;
			isfold=true;
		}
		else
		{
			isfold=false;
		}
		JSONObject job_pre = new JSONObject();
		if(isfold)
		{
			job_pre.put("time", pre);
			job_pre.put("file", "");
			job_pre.put("sys", "");
			job_pre.put("node", "");
			job_pre.put("info", "");
			job_pre.put("pre", "");
			job_pre.put("ptime", -1);
			array_data.add(job_pre);
		}
		JSONObject job = new JSONObject();
		job.put("time", time);
		job.put("file", file);
		job.put("sys", sys);
		job.put("node", node);
		job.put("info", info);
		job.put("pre", predit);
		job.put("ptime", pre);
		System.out.println(job);
		array_data.add(job);
		
	}
	JSONObject value_job = new JSONObject();
	value_job.put("code", 0);
	value_job.put("msg", "ok");
	value_job.put("data", array_data);
	value_job.put("count", 11);
	System.out.println(value_job);
	System.out.println("AAA");
	fh.createJsonFile(value_job.toString(), Config.checklog_json, "data_root");
	return value_job;

}
}
