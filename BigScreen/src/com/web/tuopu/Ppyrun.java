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
		//���Ի�ȡ��Ӧ�ڽӽڵ���Ϣ
//		System.out.println(get_nodeinfo("./test/1.csv","node_87"));
		
		//���Ի�ȡ�ڵ㹹������echart��json
//		System.out.println(get_csv_nodedata("./test/1.csv","node_87"));
		
//		//���Ի�ȡ����ṹ
//		System.out.println(get_nodedata());
		
//		//����Ԥ���ļ���Ϣ
//		for(int i=0;i<20;i++)
//		{
//			//�Ծ���������Ԥ��
//			List<List<String>> result=predict_csv("./test/"+i+".csv",0);
//			System.out.println(result);
//		}
//		System.out.println("-----------------------------------");
//		for(int i=0;i<20;i++)
//		{
//			//�Ծ���������㷨Ԥ��
//			List<List<String>> result=predict_csv("./test/"+i+".csv",2);
//			System.out.println(result);
//		}
		
		//���Ի�ȡcsv�ļ���Ϣ
//		System.out.println(get_csvinfo("./test/1.csv"));
		
		//����Ԥ������csv�ļ�
//		System.out.println(predict_to_csv("./test/1.csv","C:\\Users\\Halo\\Desktop",0));
		
		//���Է��͸澯��Ϣ
//		System.out.println(send_warning("quick test","node_22","�澯��Ϣ��ʾ��xxxxxxxxxxxxxxxxxxxxxxx����־�ļ�δ�ҵ�",sh.getNowDate()));
		
		//���Է����Զ�����Ϣ
//		System.out.println(send_info("���ٵ��ò���"));
	}
	
	//��󶨵�QQȺ�����澯��Ϣ
	public static String send_warning(String file,String node,String warning,String time)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("9"+file+"|"+node+"|"+warning+"|"+time);
		return predict_result;
	}
	
	//�����Զ�����Ϣ
	public static String send_info(String info)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("8"+info);
		return predict_result;
	}
	
	
	
	//��ýڵ�json��Ϣ
	public static String get_csv_nodedata(String csvfile,String pointnode)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("3"+csvfile+"|"+pointnode);
		return predict_result;
	}
	
	
	//��ýڵ�json��Ϣ
	public static String get_nodedata()
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("2");
        return predict_result;
	}
	
	//��ȡCSV��Ӧ����Ϣ�������״γ���˳����Ϣ(���һ��)
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
	
	//Ԥ�Ⲣ�����Ӧ��CSV�ļ���typeѡ����㷨ģʽ0������ 1BRNN 2CNN
	public static String predict_to_csv(String csvfile,String outdir,Integer type)
	{
		SocketPy clientTest=new SocketPy(socket_url, socket_port);
		String predict_result=clientTest.execCommand("5"+csvfile+"|"+outdir+"|"+type);
        return predict_result;
	}
	
	
	
	//List�� ��0��������ǰ���ڵ� ��1�������Ƕ�Ӧǰ��ϵͳ�� ��2�������Ǻ����ڵ� ��3�������Ǻ���ϵͳ�� ��ֵ��ΪString
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
	
	//List�� ��0��������ϵͳ�� ��1�������������� ��2�������Ǿ�����Ϣ ��3��������ʱ�� ��4�������Ǹ��� ��ֵ��ΪString
	//type��ʾԤ�����õ��㷨���� 0��ʾ����GBDTֱ��ͼ�����㷨�ľ������㷨 1��ʾʹ��BRNN�㷨 2��ʾʹ��CNN
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
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
	}
	public static void runFinish(OutputStream outstream)
	{
		try {
			outstream.flush();
			outstream.close();
		} catch (IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		
	}
}
