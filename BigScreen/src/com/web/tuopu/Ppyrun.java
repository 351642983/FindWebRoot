package com.web.tuopu;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;


public class Ppyrun {
	static final String socket_url="127.0.0.1";
	static final int socket_port=50007;
	
	static StringHandle sh =new StringHandle();
	static final String workspace=Config.workspace;
	public static void main(String args[])
	{
//		DataServlet.createMontiorInfoJson(Config.checklog_json, "test.json");
		//测试获取对应邻接节点信息
//		System.out.println(get_nodeinfo("./test/1.csv","node_87"));
		
		//测试获取节点构建网络echart的json
//		System.out.println(get_csv_nodedata("./test/1.csv","node_87"));
		
//		//测试获取网络结构
//		System.out.println(get_nodedata());
		
//		//测试预测文件信息
//		for(int i=0;i<20;i++)
//		{
//			//以决策树方法预测
//			List<List<String>> result=predict_csv("./test/"+i+".csv",0);
//			System.out.println(result);
//		}
//		System.out.println("-----------------------------------");
//		for(int i=0;i<20;i++)
//		{
//			//以卷积神经网络算法预测
//			List<List<String>> result=predict_csv("./test/"+i+".csv",2);
//			System.out.println(result);
//		}
		
		//测试获取csv文件信息
//		System.out.println(get_csvinfo("./test/1.csv"));
		
		//测试预测生成csv文件
//		System.out.println(predict_to_csv("./test/1.csv","C:\\Users\\Halo\\Desktop",0));
		
		//测试发送告警信息
//		System.out.println(send_warning("quick test","node_22","告警信息提示，xxxxxxxxxxxxxxxxxxxxxxx，日志文件未找到",sh.getNowDate()));
		
		//测试发送自定义信息
//		System.out.println(send_info("快速调用测试"));
	}
	
	//向绑定的QQ群发出告警信息
	public static String send_warning(String file,String node,String warning,String time)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("9"+file+"|"+node+"|"+warning+"|"+time);
		return predict_result;
	}
	
	//发送自定义信息
	public static String send_info(String info)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("8"+info);
		return predict_result;
	}
	
	
	
	//获得节点json信息
	public static String get_csv_nodedata(String csvfile,String pointnode)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("3"+csvfile+"|"+pointnode);
		return predict_result;
	}
	
	
	//获得节点json信息
	public static String get_nodedata()
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("2");
        return predict_result;
	}
	
	//获取CSV对应的信息，包括首次出现顺序信息(最后一项)
	public static List<List<String>> get_csvinfo(String csvfile)
	{


		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("6"+csvfile);
		List<List<String>> outputlist=null;
		
		String []spilt_result=predict_result.split("\\], \\[");
		if(spilt_result[0].length()>=1)
			spilt_result[0]=spilt_result[0].substring(1);
		if(spilt_result[spilt_result.length-1].length()>=3)
			spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-3);
		else{
			outputlist=new ArrayList<List<String>>();
			//spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-1);
		}

		if(outputlist==null)
			outputlist=sh.StringSplitByExpToStringList(sh.StringNlistToStringList(spilt_result), ", ");
		return outputlist;
	}
	
	//预测并输出对应的CSV文件：type选择的算法模式0决策树 1BRNN 2CNN
	public static String predict_to_csv(String csvfile,String outdir,Integer type)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("5"+csvfile+"|"+outdir+"|"+type);
        return predict_result;
	}
	
	
	
	//List中 第0个数据是前驱节点 第1个数据是对应前驱系统号 第2个数据是后驱节点 第3个数据是后驱系统号 其值均为String
	public static List<List<String>> get_nodeinfo(String csvfile,String pointnode)
	{

		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("4"+csvfile+"|"+pointnode);
		List<List<String>> outputlist=null;
		
		String []spilt_result=predict_result.split("\\], \\[");
		if(spilt_result[0].length()>=1)
			spilt_result[0]=spilt_result[0].substring(1);
		if(spilt_result[spilt_result.length-1].length()>=3)
			spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-3);
		else{
			outputlist=new ArrayList<List<String>>();
			//spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-1);
		}
		
		if(outputlist==null)
			outputlist=sh.StringSplitByExpToStringList(sh.StringNlistToStringList(spilt_result), ", ");
		return outputlist;
	}
	
	//List中 第0个数据是系统号 第1个数据是主机号 第2个数据是警告信息 第3个数据是时间 第4个数据是概率 其值均为String
	//type表示预测所用的算法类型 0表示基于GBDT直方图均衡算法的决策树算法 1表示使用BRNN算法 2表示使用CNN
	public static List<List<String>> predict_csv(String filename,Integer type)
	{


        SocketPy clientTest=new SocketPy(socket_url, socket_port);
        String predict_result=clientTest.execCommand("1"+filename+"|"+type);
        predict_result=predict_result.replace("'", "");
		List<List<String>> outputlist=null;
		String []spilt_result=predict_result.split("\\], \\[");
		if(spilt_result[0].length()>=1)
		{
			spilt_result[0]=spilt_result[0].substring(1);
		}
		if(spilt_result[spilt_result.length-1].length()>=3)
			spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-3);
		else{
			outputlist=new ArrayList<List<String>>();
			//spilt_result[spilt_result.length-1]=spilt_result[spilt_result.length-1].substring(0,spilt_result[spilt_result.length-1].length()-1);
		}

		if(outputlist==null)
			outputlist=sh.StringSplitByExpToStringList(sh.StringNlistToStringList(spilt_result), ", ");
		return outputlist;
	}
	public static void runOutput(OutputStream outstream,String command)
	{
		try {
//			outstream.write((new String(command.getBytes("utf-8"),"GBK")+"\r\n").getBytes("GBK"));
			outstream.write((command+"\r\n").getBytes("UTF-8"));
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
