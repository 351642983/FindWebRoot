package com.python;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardWatchEventKinds;
import java.nio.file.WatchEvent;
import java.nio.file.WatchKey;
import java.nio.file.WatchService;

import com.web.tuopu.Config;
public class Watch {
//	public static void main(String[] args) {
//		System.out.println("���ü���");
//		//MONITOR();
//		remove("D:\\ATEST\\AAA\\�½� Microsoft Word �ĵ�.docx","D:\\\\ATEST");
//	}
	//copy("D:\\ATEST\\�½��ļ���\\�½� Microsoft Word �ĵ�.docx","D:\\ATEST\\AAA");
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
	public static void MONITOR()
	{
		try{

			//����һ����������
			WatchService service=FileSystems.getDefault().newWatchService();
			//����·��
			Path path=Paths.get(Config.checkdir);
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
}
