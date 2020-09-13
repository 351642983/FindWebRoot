package com.util.file;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.LineNumberReader;
import java.io.OutputStreamWriter;
import java.io.RandomAccessFile;
import java.io.Writer;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;
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
	
	static void copy(String srcPathStr, String desPathStr)
	{
        //��ȡԴ�ļ�������
        String newFileName = srcPathStr.substring(srcPathStr.lastIndexOf("\\")+1); //Ŀ���ļ���ַ
        System.out.println("Դ�ļ�:"+newFileName);
        desPathStr = desPathStr + File.separator + newFileName; //Դ�ļ���ַ
        System.out.println("Ŀ���ļ���ַ:"+desPathStr);
        try
		{
             FileInputStream fis = new FileInputStream(srcPathStr);//��������������
             FileOutputStream fos = new FileOutputStream(desPathStr); //�������������               
             byte datas[] = new byte[1024*8];//�������˹���
             int len = 0;//��������   
             while((len = fis.read(datas))!=-1)//ѭ����ȡ����
			{
				fos.write(datas,0,len);
            } 
                fis.close();//�ͷ���Դ
                fis.close();//�ͷ���Դ
        }
			catch (Exception e)
			{
                e.printStackTrace();
            }
    }
  static void remove(String srcPath,String ToPath)
  {
	  try
		{
			File file=new File(srcPath); //Դ�ļ�
			if (file.renameTo(new File(ToPath+'\\'+file.getName()))) //Դ�ļ��ƶ���Ŀ���ļ�Ŀ¼
			{
				System.out.println("File is moved successful!");//����ƶ��ɹ�
			}
			else
			{
				System.out.println("File is failed to move !");//����ƶ�ʧ��
			}
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
  }
  //β��׷�Ӷ�д

  public static void Intxt(String file, String conent) {
	  BufferedWriter out = null;
	  try {
	  out = new BufferedWriter(new OutputStreamWriter(
	  new FileOutputStream(file, true)));
	  out.write(conent+"\r\n");
	  } catch (Exception e) {
	  e.printStackTrace();
	  } finally {
	  try {
	  out.close();
	  } catch (IOException e) {
	  e.printStackTrace();
	  }
	  }
	  }

  public static void writeTest(String file, String conent){        
      try {

          FileWriter fw = new FileWriter(file);
          fw.write(conent);            
          fw.close();
      } catch (IOException e) {
          e.printStackTrace();
      }
  }
  public static void MONITOR()
{
	try{

	//����һ����������
	WatchService service=FileSystems.getDefault().newWatchService();
	//����·��
	Path path=Paths.get("D:\\ATEST");
	//ע�������
	path.register(service, StandardWatchEventKinds.ENTRY_CREATE,StandardWatchEventKinds.ENTRY_DELETE,StandardWatchEventKinds.ENTRY_MODIFY);

	WatchKey watchKey;

	//ʹ��dowhile
	do{
	//��ȡһ��watch key
	watchKey=service.take();
	for(WatchEvent<?> event:watchKey.pollEvents()){
	//���ʱ���б�Ϊ�գ���ӡ�¼�����
	WatchEvent.Kind<?> kind=event.kind();
	Path eventPath=(Path)event.context();
	System.out.println(eventPath+":"+kind+":"+eventPath);

	}
	System.out.println("Ŀ¼���ݷ����ı�");

	}while(watchKey.reset());
	}catch(Exception e){
	e.printStackTrace();

	}

	// 1��ͨ��FileSystems.getDefault().newWatchService()����һ����������
	// 2������·����
	// 3����Ŀ¼ע��һ����������
	// 4��֮�����ѭ�����ȴ�watch key��
	// 5����ʱ������¼�������ͨ��watchkey��pollevent()������ȡ��
	// 6��֮����Զ�event����
}
  public static boolean createJsonFile(String jsonString, String filePath, String fileName) {
	    // ����ļ������Ƿ�ɹ�
	    boolean flag = true;

	    // ƴ���ļ�����·��
	    String fullPath = filePath + File.separator + fileName + ".json";

	    // ����json��ʽ�ļ�
	    try {
	        // ��֤����һ�����ļ�
	        File file = new File(fullPath);
	        if (!file.getParentFile().exists()) { // �����Ŀ¼�����ڣ�������Ŀ¼
	            file.getParentFile().mkdirs();
	        }
	        if (file.exists()) { // ����Ѵ���,ɾ�����ļ�
	            file.delete();
	        }
	        file.createNewFile();

	        if(jsonString.indexOf("'")!=-1){  
	            //��������ת��һ�£���ΪJSON���е��ַ������Ϳ��Ե�������������  
	            jsonString = jsonString.replaceAll("'", "\\'");  
	        }  
	        if(jsonString.indexOf("\"")!=-1){  
	            //��˫����ת��һ�£���ΪJSON���е��ַ������Ϳ��Ե�������������  
	            jsonString = jsonString.replaceAll("\"", "\\\"");  
	        }  
	          
	        if(jsonString.indexOf("\r\n")!=-1){  
	            //���س�����ת��һ�£���ΪJSON�����ַ������ܳ�����ʽ�Ļس�����  
	            jsonString = jsonString.replaceAll("\r\n", "\\u000d\\u000a");  
	        }  
	        if(jsonString.indexOf("\n")!=-1){  
	            //������ת��һ�£���ΪJSON�����ַ������ܳ�����ʽ�Ļ���  
	            jsonString = jsonString.replaceAll("\n", "\\u000a");  
	        }  
	        
	        // ��ʽ��json�ַ���
	        jsonString = JsonFormatTool.formatJson(jsonString);

	        // ����ʽ������ַ���д���ļ�
	        Writer write = new OutputStreamWriter(new FileOutputStream(file), "UTF-8");
	        write.write(jsonString);
	        write.flush();

	    } catch (Exception e) {
	        flag = false;
	        e.printStackTrace();
	    }

	    // �����Ƿ�ɹ��ı��
	    return flag;
	}
}
