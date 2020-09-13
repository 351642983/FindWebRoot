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

	//是否以追加的形式导出文件
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
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		
	}
	//判断文件为空
	public boolean judgeFileEmpty(String path)
	{
		File file = new File(path);
		if(file.exists() && file.length() == 0) {
		   return true;
		}
		return false;
	}
	//判断文件是否存在
	public boolean judgeFileExists(String path) {

		File file=new File(path);
		if (file.exists()) {
			return true;
		} else {
			return false;
		}

	}
	
	//导入文件时判断文件存在
	public boolean judeFileExistsNoDepend(File file) {

		if (file.exists()) {
			return true;
		} else {
			return false;
		}

	}
	
	//读取文件每一行的数据并且放在字符串容器中
	public List<String> inputFile(String path)
	{

		List<String> strlist=new ArrayList<String>();
		File a=new File(path);
		if(!judeFileExistsNoDepend(a))
		{
			System.out.println(path+"文件不存在");
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
					//line是每一行的数据
					strlist.add(line);
				}
				bufr.close();
			}
			c.close();
			b.close();
		} catch ( IOException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		
		return strlist;
	}
	
	
	//获得文件的内容行数
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
	
	
	//删除文件中的第n行数据
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
	
	
	//将字符串容器以行间修饰串存入文件中
	public void outFileByStringList(List<String> strlist,String outfile,String lineDecorate)
	{
		outFile(new StringHandle().StringListIntoString(strlist, lineDecorate),outfile,false);
	}
	
	//将字符串容器以空格和行间修饰串存入文件中
	public void outFileByStringListList(List<List<String>> strlist,String outfile,String pointDecorate,String lineDecorate)
	{
		StringHandle sh=new StringHandle();
		outFile(sh.StringListIntoString(sh.StringListListIntoStringList(strlist,pointDecorate),lineDecorate ),outfile,false);
	}
	
	//获得文件的修改时间
	public String getModifiedTime(String path){  
        File f = new File(path);              
        Calendar cal = Calendar.getInstance();  
        String timechange="";
        //获取文件时间
        long time = f.lastModified();  
        SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss"); 
        //转换文件最后修改时间的格式
        cal.setTimeInMillis(time);    

        timechange = formatter.format(cal.getTime());
        return timechange;
        //输出：修改时间[2]    2009-08-17 10:32:38  
    }  
	
	//判断文件是否为空
	public boolean fileIsEmpty(String path)
	{
		File fi=new File(path);
		
		if(fi.length()==0||!fi.exists())
			return true;
		else return false;
	}
	
	//获得文件目录里面的信息转为字符串的容器的容器
	public List<List<String>> getInfosList(String path,String spchar)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<List<String>> objinfo=sh.StringSplitByExpToStringList(objline, spchar);;
		return objinfo;
	}
	
	//获得文件目录里面的信息转为字符串的容器的容器
	public Map<String,String> getInfosListToMap(String path,String spchar)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<List<String>> objinfo=sh.StringSplitByExpToStringList(objline, spchar);
		return sh.StringListToMap(sh.StringListListInitSingleList(objinfo, 0), sh.StringListListInitSingleList(objinfo, 1));
	}
	
	//获得文件目录里面的信息转为对应类的容器
	public <T> List<T> getInfosToTlist(String path,String []nameNlist,Class<T> clazz)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<T> objinfo=sh.StringSplitByExpToTList(objline, " ",nameNlist,clazz);;
		return objinfo;
	}
	
	//获得文件目录的里面的信息转为对应类的容器(自动型)
	public <T> List<T> getInfosToTlist(String path,Class<T> clazz)
	{
		StringHandle sh=new StringHandle();
		List<String> objline=null;
		objline=inputFile(path);
		List<T> objinfo=sh.StringSplitByExpToTList(objline, " ",clazz);;
		return objinfo;
	}
	
	//将对应类容器里面的所有数据存入对应文件中
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
	
	
	//将对应的类数据添加到对应文件中
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
	
	//获得文件目录下所有文件
	public List<String> getFileList(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// 获取目录下的所有文件或文件夹
		if (files == null) {// 如果目录为空，直接退出
			return null;
		}

		// 遍历，目录下的所有文件
		for (File f : files) {
			if (f.isFile()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO 自动生成的 catch 块
					e.printStackTrace();
				}
			} 
		}
		return fileList;
	}
	//获得文件目录下所有文件(包括递归子文件夹的文件)
	public List<String> getFileListAll(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// 获取目录下的所有文件或文件夹
		if (files == null) {// 如果目录为空，直接退出
			return null;
		}

		// 遍历，目录下的所有文件
		for (File f : files) {

			if (f.isFile()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO 自动生成的 catch 块
					e.printStackTrace();
				}
			} else if (f.isDirectory()) {
				//System.out.println(f.getAbsolutePath());
				fileList.addAll(getFileList(f.getAbsolutePath()));
			}
		}
		return fileList;
	}
	
	//获得文件目录下所有文件夹
	public List<String> getDirList(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// 获取目录下的所有文件或文件夹
		if (files == null) {// 如果目录为空，直接退出
			return null;
		}

		// 遍历，目录下的所有文件
		for (File f : files) {
			if (f.isDirectory()) {
				try {
					fileList.add(f.getCanonicalPath());
				} catch (IOException e) {
					// TODO 自动生成的 catch 块
					e.printStackTrace();
				}
			} 
		}
		return fileList;
	}
	
	//获得文件目录下所有文件夹(包括递归子文件夹的文件)
	public List<String> getDirListAll(String fileDir)
	{

		List<String> fileList = new ArrayList<String>();
		File file = new File(fileDir);
		File[] files = file.listFiles();// 获取目录下的所有文件或文件夹
		if (files == null) {// 如果目录为空，直接退出
			return null;
		}

		// 遍历，目录下的所有文件
		for (File f : files) {
			if (f.isDirectory()) {
				String nowDir=null;
				try {
					nowDir=f.getCanonicalPath();
					fileList.add(nowDir);
				} catch (IOException e) {
					// TODO 自动生成的 catch 块
					e.printStackTrace();
				}
				List<String> initDir=getDirListAll(nowDir);
				if(initDir.size()!=0)
					fileList.addAll(initDir);
			} 
		}
		return fileList;
	}
	
	//创建文件夹
	public boolean createDir(String Path)
	{
		String filePar = Path;// 文件夹路径  
        File myPath = new File( filePar );  
        if ( !myPath.exists()){//若此目录不存在，则创建之  
            myPath.mkdir();  
            return true;
        }
        return false;
	}
	
	
}
