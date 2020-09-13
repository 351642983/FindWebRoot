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
//		System.out.println("启用监视");
//		//MONITOR();
//		remove("D:\\ATEST\\AAA\\新建 Microsoft Word 文档.docx","D:\\\\ATEST");
//	}
	//copy("D:\\ATEST\\新建文件夹\\新建 Microsoft Word 文档.docx","D:\\ATEST\\AAA");
	static void copy(String srcPathStr, String desPathStr)
	{
		//获取源文件的名称
		String newFileName = srcPathStr.substring(srcPathStr.lastIndexOf("\\")+1); //目标文件地址
		System.out.println("源文件:"+newFileName);
		desPathStr = desPathStr + File.separator + newFileName; //源文件地址
		System.out.println("目标文件地址:"+desPathStr);
		try
		{
			FileInputStream fis = new FileInputStream(srcPathStr);//创建输入流对象
			FileOutputStream fos = new FileOutputStream(desPathStr); //创建输出流对象               
			byte datas[] = new byte[1024*8];//创建搬运工具
			int len = 0;//创建长度   
			while((len = fis.read(datas))!=-1)//循环读取数据
			{
				fos.write(datas,0,len);
			} 
			fis.close();//释放资源
			fis.close();//释放资源
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
			File file=new File(srcPath); //源文件
			if (file.renameTo(new File(ToPath+'\\'+file.getName()))) //源文件移动至目标文件目录
			{
				System.out.println("File is moved successful!");//输出移动成功
			}
			else
			{
				System.out.println("File is failed to move !");//输出移动失败
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

			//创建一个监听服务
			WatchService service=FileSystems.getDefault().newWatchService();
			//设置路径
			Path path=Paths.get(Config.checkdir);
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

			}while(watchKey.reset());
		}catch(Exception e){
			e.printStackTrace();

		}

		// 1、通过FileSystems.getDefault().newWatchService()创建一个监听服务；
		// 2、设置路径；
		// 3、对目录注册一个监听器；
		// 4、之后进入循环，等待watch key；
		// 5、此时如果有事件发生可通过watchkey的pollevent()方法获取；
		// 6、之后可以对event处理；
	}
}
