package com.web.tuopu;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.OutputStreamWriter;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;
import java.util.Map;


public class FileHandle {

	//�Ƿ���׷�ӵ���ʽ�����ļ�
	public void outFile(String txt,String outfile,boolean isappend)
	{
		File fi=new File(outfile);
		FileOutputStream fop;
		try {
			fop = new FileOutputStream(fi,isappend);
			OutputStreamWriter ops=new OutputStreamWriter(fop,"UTF-8");
			ops.append(txt);
			ops.close();
			fop.close();
		} catch (IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		
	}
	//�ж��ļ�Ϊ��
	public boolean judgeFileEmpty(String path)
	{
		File file = new File(path);
		if(file.exists() && file.length() == 0) {
		   return true;
		}
		return false;
	}
	//�ж��ļ��Ƿ����
	public boolean judgeFileExists(String path) {

		File file=new File(path);
		if (file.exists()) {
			return true;
		} else {
			return false;
		}

	}
	
	//�����ļ�ʱ�ж��ļ�����
	public boolean judeFileExistsNoDepend(File file) {

		if (file.exists()) {
			return true;
		} else {
			return false;
		}

	}
	
	//��ȡ�ļ�ÿһ�е����ݲ��ҷ����ַ���������
	public List<String> inputFile(String path)
	{

		List<String> strlist=new ArrayList<String>();
		File a=new File(path);
		if(!judeFileExistsNoDepend(a))
		{
			System.out.println(path+"�ļ�������");
			return strlist;
		}
		FileInputStream b;
		try {
			b = new FileInputStream(a);
			InputStreamReader c=new InputStreamReader(b,"UTF-8");


			{
				BufferedReader bufr =new BufferedReader(c);
				String line = null;
				while((line = bufr.readLine())!=null){
					//line��ÿһ�е�����
					strlist.add(line);
				}
				bufr.close();
			}
			c.close();
			b.close();
		} catch ( IOException e) {
			// TODO �Զ����ɵ� catch ��
			e.printStackTrace();
		}
		
		return strlist;
	}
	
	
	//����ļ�����������
	public long getLineNumber(String strfile) {
		File file=new File(strfile);
	    if (file.exists()) {
	        try {
	            FileReader fileReader = new FileReader(file);
	            LineNumberReader lineNumberReader = new LineNumberReader(fileReader);
	            lineNumberReader.skip(Long.MAX_VALUE);
	            long lines = lineNumberReader.getLineNumber() + 1;
	            fileReader.close();
	            lineNumberReader.close();
	            return lines;
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	    }
	    return 0;
	}
	
	
	//ɾ���ļ��еĵ�n������
	public String deleteLine(String filePath,int indexLine){             
		try {        
			List<String> ifList=inputFile(filePath);
			ifList.remove(indexLine);
			outFile(new StringHandle().StringListIntoString(ifList, "\r\n"),filePath,false);
		} catch (Exception e) {  
			return "fail :"+ e.getCause();     
		}      
		return "success!";   
	}
	
	
	//���ַ����������м����δ������ļ���
	public void outFileByStringList(List<String> strlist,String outfile,String lineDecorate)
	{
		outFile(new StringHandle().StringListIntoString(strlist, lineDecorate),outfile,false);
	}
	
	//���ַ��������Կո���м����δ������ļ���
	public void outFileByStringListList(List<List<String>> strlist,String outfile,String pointDecorate,String lineDecorate)
	{
		StringHandle sh=new StringHandle();
		outFile(sh.StringListIntoString(sh.StringListListIntoStringList(strlist,pointDecorate),lineDecorate ),outfile,false);
	}
	
	//����ļ����޸�ʱ��
	public String getModifiedTime(String path){  
        File f = new File(path);              
        Calendar cal = Calendar.getInstance();  
        String timechange="";
        //��ȡ�ļ�ʱ��
        long time = f.lastModified();  
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
        //ת���ļ�����޸�ʱ��ĸ�ʽ
        cal.setTimeInMillis(time);    

        timechange = formatter.format(cal.getTime());
        return timechange;
        //������޸�ʱ��[2]    2009-08-17 10:32:38  
    }  
	
	//�ж��ļ��Ƿ�Ϊ��
	public boolean fileIsEmpty(String path)
	{
		File fi=new File(path);
		
		if(fi.length()==0||!fi.exists())
			return true;
		else return false;
	}
	
	//����ļ�Ŀ¼�������ϢתΪ�ַ���������������
	public List<List<String>> getInfosList(String path,String spchar)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<List<String>> objinfo=sh.StringSplitByExpToStringList(objline, spchar);;
		return objinfo;
	}
	
	//����ļ�Ŀ¼�������ϢתΪ�ַ���������������
	public Map<String,String> getInfosListToMap(String path,String spchar)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<List<String>> objinfo=sh.StringSplitByExpToStringList(objline, spchar);
		return sh.StringListToMap(sh.StringListListInitSingleList(objinfo, 0), sh.StringListListInitSingleList(objinfo, 1));
	}
	
	//����ļ�Ŀ¼�������ϢתΪ��Ӧ�������
	public <T> List<T> getInfosToTlist(String path,String []nameNlist,Class<T> clazz)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<T> objinfo=sh.StringSplitByExpToTList(objline, " ",nameNlist,clazz);;
		return objinfo;
	}
	
	//����ļ�Ŀ¼���������ϢתΪ��Ӧ�������(�Զ���)
	public <T> List<T> getInfosToTlist(String path,Class<T> clazz)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<T> objinfo=sh.StringSplitByExpToTList(objline, " ",clazz);;
		return objinfo;
	}
	
	//����Ӧ������������������ݴ����Ӧ�ļ���
	public <T> void outputFileByTlist(List<T> obj,Class<?> clazz,String path,boolean isAppend)
	{
		EntityToString ets=new EntityToString();
		StringHandle sh=new StringHandle();
		if(fileIsEmpty(path))
			outFile(sh.StringListIntoString(ets.getStringList(obj, clazz),"\r\n"),path,isAppend);
		else outFile("\r\n"+sh.StringListIntoString(ets.getStringList(obj, clazz),"\r\n"),path,isAppend);
	}
	public <T> void outputFileByTlist(List<T> obj,String path,boolean isAppend)
	{
		outputFileByTlist(obj,obj.get(0).getClass(),path,isAppend);
	}
	
	
	//����Ӧ����������ӵ���Ӧ�ļ���
	public <T> void outputFileByT(T obj,Class<?> clazz,String path,boolean isAppend)
	{
		EntityToString ets=new EntityToString();
		if(fileIsEmpty(path))
			outFile(ets.getString(obj, clazz),path,isAppend);
		else outFile("\r\n"+ets.getString(obj, clazz),path,isAppend);
	}
	
	public <T> void outputFileByT(T obj,String path,boolean isAppend)
	{
		outputFileByT(obj,obj.getClass(),path,isAppend);
	}
	
	//����ļ�Ŀ¼�������ļ�
	public List<String> getFileList(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// ��ȡĿ¼�µ������ļ����ļ���
		if (files == null) {// ���Ŀ¼Ϊ�գ�ֱ���˳�
			return null;
		}

		// ������Ŀ¼�µ������ļ�
		for (File f : files) {
			if (f.isFile()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO �Զ����ɵ� catch ��
					e.printStackTrace();
				}
			} 
		}
		return fileList;
	}
	//����ļ�Ŀ¼�������ļ�(�����ݹ����ļ��е��ļ�)
	public List<String> getFileListAll(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// ��ȡĿ¼�µ������ļ����ļ���
		if (files == null) {// ���Ŀ¼Ϊ�գ�ֱ���˳�
			return null;
		}

		// ������Ŀ¼�µ������ļ�
		for (File f : files) {

			if (f.isFile()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO �Զ����ɵ� catch ��
					e.printStackTrace();
				}
			} else if (f.isDirectory()) {
				//System.out.println(f.getAbsolutePath());
				fileList.addAll(getFileList(f.getAbsolutePath()));
			}
		}
		return fileList;
	}
	
	//����ļ�Ŀ¼�������ļ���
	public List<String> getDirList(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// ��ȡĿ¼�µ������ļ����ļ���
		if (files == null) {// ���Ŀ¼Ϊ�գ�ֱ���˳�
			return null;
		}

		// ������Ŀ¼�µ������ļ�
		for (File f : files) {
			if (f.isDirectory()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO �Զ����ɵ� catch ��
					e.printStackTrace();
				}
			} 
		}
		return fileList;
	}
	
	//����ļ�Ŀ¼�������ļ���(�����ݹ����ļ��е��ļ�)
	public List<String> getDirListAll(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// ��ȡĿ¼�µ������ļ����ļ���
		if (files == null) {// ���Ŀ¼Ϊ�գ�ֱ���˳�
			return null;
		}

		// ������Ŀ¼�µ������ļ�
		for (File f : files) {
			if (f.isDirectory()) {
				String nowDir=null;
				try {
					nowDir=f.getCanonicalPath();
					fileList.add(nowDir);
				} catch (IOException e) {
					// TODO �Զ����ɵ� catch ��
					e.printStackTrace();
				}
				List<String> initDir=getDirListAll(nowDir);
				if(initDir.size()!=0)
					fileList.addAll(initDir);
			} 
		}
		return fileList;
	}
	
	//�����ļ���
	public boolean createDir(String Path)
	{
		String filePar = Path;// �ļ���·��  
        File myPath = new File( filePar );  
        if ( !myPath.exists()){//����Ŀ¼�����ڣ��򴴽�֮  
            myPath.mkdir();  
            return true;
        }
        return false;
	}
	
	
}
