package com.web.tuopu;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.google.gson.Gson;
import com.watch.Check_watch;
import com.watch.Watch;
import com.web.entity.LightInfo;
import com.web.entity.RootInfo;
import org.apache.commons.io.FileUtils;
/**
 * Servlet implementation class DataServlet
 */
@WebServlet("/DataServlet")
public class DataServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	static FileHandle fh=new FileHandle();
	static StringHandle sh=new StringHandle();
	static String monthdatadir=Config.monthdatadir;
	static Check_watch cw=null;
	static boolean watch_have=false;
	static boolean warch_condition=false;
	static String newrootinfo=new String();
	static Gson gson=new Gson();
	static String webconditioninfo=new String();
	static final String FoldPath=Config.checkdir;
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public DataServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getWriter().append("Served at: ").append(request.getContextPath());
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO 自动生成的方法存根
		super.service(request, response);
		request.setCharacterEncoding("utf-8");
		String method=request.getParameter("method");
//		test
//		getRootNumJson(request,response);
//		haveCheckedRoot("./test/1.csv",false);
//		getCurrentMonthRootInfo(request,response);
//		getNewHistoryRoot(request,response);
		
		if(method==null)
			return;
		if(method.equals("getRootNumJson"))
		{
			getRootNumJson(request,response);
		}
		else if(method.equals("getCurrentMonthRootInfo"))
		{
			getCurrentMonthRootInfo(request,response);
		}
		else if(method.equals("getNewHistoryRoot"))
		{
			getNewHistoryRoot(request,response);
		}
		else if(method.equals("getNodeJson"))
		{
			getNodeJson(request,response);
		}
		else if(method.equals("getCsvNodeJson"))
		{
			getCsvNodeJson(request,response);
		}else if(method.equals("getWebCondition"))
		{
			getWebCondition(request,response);
		}else if(method.equals("runCheck"))
		{
			runCheckWeb(request,response);
		}else if(method.equals("resetLog"))
		{
			resetLog(request,response);
		}else if(method.equals("rescan"))
		{
			rescan(request,response);
		}else if(method.equals("OpenCheckDir"))
		{
			OpenCheckDir(request,response);
		}else if(method.equals("OpenTestDir"))
		{
			OpenTestDir(request,response);
		}
	}
	private void runCheckWeb(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		runCheck(!isCheckRunning());
	}
	private void OpenCheckDir(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		runCheck(!isCheckRunning());
		try {
            java.awt.Desktop.getDesktop().open(new File(Config.checkdir));
        } catch (IOException e) {
            e.printStackTrace();
        }
		response.getWriter().print("ok");
	}
	private void OpenTestDir(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		runCheck(!isCheckRunning());
		try {
            java.awt.Desktop.getDesktop().open(new File(Config.workspace+"/"+"test"));
        } catch (IOException e) {
            e.printStackTrace();
        }
		response.getWriter().print("ok");
	}
	private void resetLog(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		File file=new File(monthdatadir+"/rootlog.txt"); //源文件
		file.delete();
		//xg base
		fh.outFile("2490 81914 11 5 7 9 4 8 6 84404", monthdatadir+"/info_total.txt", false);
		newrootinfo="";
	}
	private void rescan(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		List<String> filelist=fh.getFileList(Config.checkdir);
		for(String init:filelist)
		{
			haveCheckedRoot(init,true,null);
		}
		
	}
	private void getNodeJson(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		response.getWriter().write(Ppyrun.get_nodedata());
	}
	private void getCsvNodeJson(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		response.getWriter().write(Ppyrun.get_csv_nodedata(request.getParameter("csvfile"), request.getParameter("pointnode")));
	}
	private void getWebCondition(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		response.getWriter().write(webconditioninfo);
	}
	private void getRootNumJson(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RootInfo ri=new RootInfo();
		if(!fh.judgeFileExists(monthdatadir+""))
			fh.createDir(monthdatadir+"");
		List<String> infos=sh.StringNlistToStringList(fh.inputFile(monthdatadir+"/info_total.txt").get(0).split(" "));
		Gson gson=new Gson();
		ri.setRootnum(Integer.parseInt(infos.get(0)));
		ri.setUnrootnum(Integer.parseInt(infos.get(1)));
		ri.setMonday(Integer.parseInt(infos.get(2)));
		ri.setTuesday(Integer.parseInt(infos.get(3)));
		ri.setWednesday(Integer.parseInt(infos.get(4)));
		ri.setThursday(Integer.parseInt(infos.get(5)));
		ri.setFriday(Integer.parseInt(infos.get(6)));
		ri.setSaturday(Integer.parseInt(infos.get(7)));
		ri.setSunday(Integer.parseInt(infos.get(8)));
		ri.setTotalnum(Integer.parseInt(infos.get(9)));
		String json=gson.toJson(ri);
		response.getWriter().write(json);
	}
	
	private void getCurrentMonthRootInfo(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		Gson gson=new Gson();
//		List<Integer> numlist=new ArrayList<Integer>();
		Map<String,Integer[]> monthinfos=new HashMap<String,Integer[]>();
		String []date=sh.getNowDate().split("-");
		Integer day=Integer.parseInt(date[2]);
		if(!fh.judgeFileExists(monthdatadir+""))
			fh.createDir(monthdatadir+"");
		if(!fh.judgeFileExists(monthdatadir+"/"+date[0]+"-"+date[1]+".txt"))
		{
			List<Integer> temp_li=new ArrayList<Integer>();
			for(int i=0;i<day;i++)
			{
				if(i!=day-1)
					fh.outFile(0+"\r\n", monthdatadir+"/"+date[0]+"-"+date[1]+".txt", true);
				else fh.outFile(0+"", monthdatadir+"/"+date[0]+"-"+date[1]+".txt", true);
				temp_li.add(0);
			}
			Integer[] inlist = new Integer[day];
			monthinfos.put("data", temp_li.toArray(inlist));
		}
		else
		{
			List<Integer> monthdata=sh.StringListToIntegerList(fh.inputFile(monthdatadir+"/"+date[0]+"-"+date[1]+".txt"));
			if(monthdata.size()<day)
			{
				for(int i=0;i<day-monthdata.size();i++)
				{
					fh.outFile("\r\n"+0, monthdatadir+"/"+date[0]+"-"+date[1]+".txt", true);
				}
			}
			monthdata=sh.StringListToIntegerList(fh.inputFile(monthdatadir+"/"+date[0]+"-"+date[1]+".txt"));
			
			Integer[] inlist = new Integer[day];
			
			monthinfos.put("data",monthdata.subList(0, day).toArray(inlist));
		}
		String data =gson.toJson(monthinfos);
		response.getWriter().write(data);
		
	}
	//monthdata/rootlog.txt 检测到的根因最新信息    monthdata/info_total.txt 检测的相关统计历史信息
	//均在桌面 其中info_total.txt不会自动生成
	//加判别函数	是否以现在的检测时间未标准，否则以文件中的时间
	public static void haveCheckedRoot(String csvfilep,boolean nowtime,String movetofile)
	{
		String csvfile=null;
		if(csvfilep.startsWith("./"))
		{
			csvfile=Config.workspace+csvfilep.substring(1);
		}
		else csvfile=csvfilep;
		List<List<String>> predict_result=Ppyrun.predict_csv(csvfile,Config.ptype);
		if(!fh.judgeFileExists(monthdatadir+""))
			fh.createDir(monthdatadir+"");
		
		//0根因文件 1非根因文件 2-8周一至周日 9总检测文件数量
		List<Integer> infos=sh.StringListToIntegerList(sh.StringNlistToStringList(fh.inputFile(monthdatadir+"/info_total.txt").get(0).split(" ")));
		//xg totalnum root
		Integer totallinenum=(int) (fh.getLineNumber(csvfile)-1);
		infos.set(9, infos.get(9)+totallinenum);
		//xg add
		Integer rootresult=0;
		if(predict_result.size()==0)
		{
			//xg unroot
			infos.set(1, infos.get(1)+totallinenum);
			fh.outFile(sh.IntegerListIntoString(infos, " "), monthdatadir+"/info_total.txt", false);
			if(movetofile!=null)
			{
				File file=new File(csvfile); //源文件
				try {
					FileUtils.moveFile(file,new File(movetofile));
					System.out.println("move success");
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return;
		}
		else { //xg add
			String nodename="主机node_"+predict_result.get(0).get(1);
			rootresult=sh.StringListGetSuitSubExpStringList(fh.inputFile(csvfile), nodename).size();
			infos.set(1, infos.get(1)+totallinenum-rootresult);
			
		}
		
		//List中 第0个数据是系统号 第1个数据是主机号 第2个数据是警告信息 第3个数据是时间 第4个数据是概率 其值均为String
		List<String> rootinfo=predict_result.get(0);
		
		Ppyrun.send_warning(csvfilep,rootinfo.get(1), rootinfo.get(2).replace("\'", ""), sh.getNowDate());
		
		String month="";
		Integer day=0;
		Integer week=0;
		if(!nowtime)
		{
			month=sh.DateToAnotherDateFormat(rootinfo.get(3).substring(1,rootinfo.get(3).length()-1), "yyyy-MM-dd HH:mm:ss", "yyyy-MM");
			day=Integer.parseInt(sh.DateToAnotherDateFormat(rootinfo.get(3).substring(1,rootinfo.get(3).length()-1), "yyyy-MM-dd HH:mm:ss", "dd"));
			week=sh.dateToWeek(rootinfo.get(3).substring(1,rootinfo.get(3).length()-1), "yyyy-MM-dd HH:mm:ss")+1;
			
		}
		else
		{
			month=sh.DateToAnotherDateFormat(sh.getNowDate(), "yyyy-MM-dd", "yyyy-MM");
			day=Integer.parseInt(sh.DateToAnotherDateFormat(sh.getNowDate(), "yyyy-MM-dd", "dd"));
			week=sh.dateToWeek(rootinfo.get(3).substring(1,rootinfo.get(3).length()-1), "yyyy-MM-dd HH:mm:ss")+1;
		}
		//xg root
		infos.set(0, infos.get(0)+rootresult);
		
		
		infos.set(week, infos.get(week)+1);
		fh.outFile(sh.IntegerListIntoString(infos, " "), monthdatadir+"/info_total.txt", false);
		if(!fh.judgeFileExists(monthdatadir+"/"+month+".txt"))
		{
			List<Integer> temp_li=new ArrayList<Integer>();
			for(int i=0;i<day;i++)
			{
				if(i!=day-1) {
					fh.outFile(0+"\r\n", monthdatadir+"/"+month+".txt", true);
				}
				else {
					fh.outFile(1+"", monthdatadir+"/"+month+".txt", true);
				}
				temp_li.add(0);
			}
		}
		else
		{
			List<Integer> monthdata=sh.StringListToIntegerList(fh.inputFile(monthdatadir+"/"+month+".txt"));
			if(monthdata.size()<day)//天数不够
			{
				for(int i=0;i<day-monthdata.size();i++)
				{
					if(i!=day-monthdata.size()-1)
					{
						fh.outFile("\r\n"+0, monthdatadir+"/"+month+".txt", true);
					}
					else
					{
						fh.outFile("\r\n"+1+"", monthdatadir+"/"+month+".txt", true);
					}
				}
			}
			else	//足够天数情况
			{
				monthdata.set(day-1, monthdata.get(day-1)+1);
				fh.outFile("", monthdatadir+"/"+month+".txt", false);
				int g_num=monthdata.size();
				for(int i=0;i<g_num;i++)
				{
					if(i!=g_num-1)
						fh.outFile(monthdata.get(i)+"\r\n", monthdatadir+"/"+month+".txt", true);
					else fh.outFile(monthdata.get(i)+"", monthdatadir+"/"+month+".txt", true);
				}
			}
		}
		
		if(movetofile!=null)
		{
			File file=new File(csvfile); //源文件
			try {
				FileUtils.moveFile(file,new File(movetofile));
				System.out.println("move success");
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		List<String> lines=fh.inputFile(monthdatadir+"/rootlog.txt");
		
		String outtxt=null;
		//检测到文件，预警列表  List中 0是文件  第1个数据是系统号 第2个数据是主机号 第3个数据是警告信息 第4个数据是时间 第5个数据是概率 第6个是python预测文件时间 其值均为String
		if(fh.judgeFileEmpty(monthdatadir+"/rootlog.txt"))
			outtxt=((movetofile==null)?csvfile:movetofile)+"|"+sh.StringListIntoString(rootinfo, "|");
		else if(fh.judgeFileExists(monthdatadir+"/rootlog.txt"))
			outtxt="\r\n"+((movetofile==null)?csvfile:movetofile)+"|"+sh.StringListIntoString(rootinfo, "|");
		else outtxt=((movetofile==null)?csvfile:movetofile)+"|"+sh.StringListIntoString(rootinfo, "|");
		if(!sh.StringListIsExContainString(lines, outtxt.replace("\r\n", "")))
		{
			fh.outFile(outtxt, monthdatadir+"/rootlog.txt", true);
		}
	}
	
	private void getNewHistoryRoot(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		if(!watch_have)
		{
			runCheck(true);
		}

		response.setContentType("text/html;charset=utf-8");
		response.getWriter().write(newrootinfo);
	}
	
	//获取预警列表
	public static void getNewHistoryRoot_handle(){
		if(!fh.judgeFileExists(monthdatadir+""))
			fh.createDir(monthdatadir+"");
		List<String> lineinfo=null;
		Map<String,String> newrootinfos=new HashMap<String,String>();
		if(fh.judgeFileExists(monthdatadir+"/rootlog.txt")&&!fh.judgeFileEmpty(monthdatadir+"/rootlog.txt"))
			lineinfo=fh.inputFile(monthdatadir+"/rootlog.txt");
		else
		{
			if(!fh.judgeFileExists(monthdatadir+"/rootlog.txt"))
				fh.outFile("", monthdatadir+"/rootlog.txt", false);
			return;
		}
		int g_rootsize=lineinfo.size();
		int c=0;
		for(int i=g_rootsize-1;i>=0;i--)
		{
			String []spiltsentence=lineinfo.get(i).split("\\|");
			if(!fh.judgeFileExists(spiltsentence[0]))
				continue;
			c+=1;
			String results="";
			try {
				results=spiltsentence[5].substring(0,6);
			}
			catch(Exception e){
				results=spiltsentence[5];
			}
			newrootinfos.put(c+"", "文件:"+spiltsentence[0]+"可能存在根因,其预测节点:<span style=\"color:red\">node_"+spiltsentence[2]+"</span><span style=\"float:right;margin-right:40px;\">预测花费时间:<span style=\"color:red\">"+spiltsentence[6].substring(0,4)+"</span>秒</span>"+"<br>对应告警信息为:<span style=\"color:red\">"+spiltsentence[3]+"</span><br>置信度为:"+results);
			newrootinfos.put(c+"f", spiltsentence[0].replace("\\", "/"));
			newrootinfos.put(c+"p", "node_"+spiltsentence[2]);
		}

		String data =gson.toJson(newrootinfos);
		newrootinfo=data;
		
		
		LightInfo li=new LightInfo();
		if(isCheckRunning())
			li.setCheck("zc");
		else li.setCheck("yc");
		if(isConnected())
			li.setWeb("zc");
		else li.setWeb("yc");
		webconditioninfo=gson.toJson(li);
		
		
		return;
//		response.setContentType("text/html;charset=utf-8");
//		response.getWriter().write(data);
	}
	
	//生成json rootinfo
	public static String createRootInfoJson()
	{
		try
		{
			//0文件位置 1系统号 2主机号 3告警 4时间 5概率
			List<List<String>> infolist=fh.getInfosList(Config.monthdatadir+"\\rootlog.txt", "\\|");
			String json="{\r\n" + 
					"   \"code\":0,\"count\":11,\"data\":\r\n" + 
					"   [";
//			System.out.println(infolist);
			for(int i=0;i<infolist.size();i++)
			{
				String dirtime=sh.DateToAnotherDateFormat(infolist.get(i).get(4), "yyyy-MM-dd HH:mm:ss", "yyyy-MM-dd HH:mm");
				json+="      {\r\n" + 
						"         \"file\":\"\",\"info\":\"\",\"node\":\"\",\"pre\":\"\",\"ptime\":-1,\"sys\":\"\",\"time\":\""+dirtime+"\"\r\n" + 
						"      },";
				json+="{\r\n" + 
						"         \"file\":\""+infolist.get(i).get(0).replace("\\", "/")+"\",\"info\":\""+infolist.get(i).get(3)+"\",\"node\":\""+infolist.get(i).get(2)+"\",\"pre\":\""+infolist.get(i).get(5)+"\",\"ptime\":\""+dirtime+"\",\"sys\":\""+infolist.get(i).get(1)+"\",\"time\":\""+infolist.get(i).get(4)+"\"\r\n" + 
						"      }";
				if(i!=infolist.size()-1)
					json+=",";
			}
			
			json+="   ],\"msg\":\"ok\"\r\n" + 
					"}";
			return json;
		}
		catch(Exception e)
		{
			return "";
		}
		
	}
	
	//生成json MontiorInfo
	public static String createMontiorInfoJson()
	{
		try
		{
			//时间（0，3）文件（1,4-n-1） 操作（2， 3） （已更新）
			List<List<String>> infolist=fh.getInfosList(Config.checklog, " ");
			
			String json="{\r\n" + 
					"   \"code\":0,\"count\":11,\"data\":\r\n" + 
					"   [";
//			System.out.println(infolist);
			String before="";
			String nowfile="";
			for(int i=0;i<infolist.size();i++)
			{
				nowfile=infolist.get(i).get(1);
				String dirtime=infolist.get(i).get(1);
				if(!nowfile.equals(before))
				{
					json+="      {\r\n" + 
							"         \"file\":\""+nowfile+"\",\"time\":\"\",\"Do\":\"\",\"pfile\":-1,\"info\":\"\"\r\n" + 
							"      },";
				}
				if(infolist.get(i).size()!=4)
				{
					json+="{\r\n" + 
							"         \"file\":\""+nowfile.substring(4,nowfile.length()-1).replace("\\", "/")+"\",\"time\":\""+infolist.get(i).get(0).substring(3)+"\",\"Do\":\""+infolist.get(i).get(2).substring(3)+"\",\"pfile\":\""+dirtime+"\",\"info\":\"\"\r\n" + 
							"      }";
				}
				else
				{
					json+="{\r\n" + 
							"         \"file\":\""+nowfile.substring(4,nowfile.length()-1).replace("\\", "/")+"\",\"time\":\""+infolist.get(i).get(0).substring(3)+"\",\"Do\":\""+infolist.get(i).get(2).substring(3)+"\",\"pfile\":\""+dirtime+"\",\"info\":\""+infolist.get(i).get(3)+"\"\r\n" + 
							"      }";
				}
				if(i!=infolist.size()-1)
					json+=",";
				
				before=nowfile;
			}

			json+="   ],\"msg\":\"ok\"\r\n" + 
					"}";

			return json;
		}
		catch(Exception e)
		{
			return "";
		}

	}
	
	//判断网络是否连通
	public static boolean isConnected()
	{
		URL url = null;  
        try {  
            url = new URL("http://baidu.com");  
            try {  
                InputStream in = url.openStream();  
                in.close();  
                return true;
            } catch (IOException e) {  
            	return false;
            }  
        } catch (MalformedURLException e) {  
            e.printStackTrace();  
        } 
        return false;
	}
	
	//判断监视器是否正在运行
	public static boolean isCheckRunning()
	{
		if(cw!=null)
			return !cw.exit;
			
		return warch_condition;
	}
	
	//运行监视器
	public static void runCheck(boolean run)
	{
		System.out.println("更改监控状态:"+run);
		warch_condition=run;
		if(watch_have)
		{
			if(run)
			{
				cw=new Check_watch();
				cw.exit=false;
				cw.start();
				
			}
			else
			{
				cw.exit=true;
				cw=null;
			}
		}
		else if(run)
		{
			cw=new Check_watch();
			cw.start();
			
			
			watch_have=true;
//			  run in a second    
			 final long timeInterval = Config.time_refresh;    
			 Runnable runnable = new Runnable() {    
				 public void run() {    
					 while (true) {    
						 // ------- code for task to run    
						 getNewHistoryRoot_handle();
						 // ------- ends here    
						 try {    
							 Thread.sleep(timeInterval);    
						 } catch (InterruptedException e) {    
							 e.printStackTrace();    
						 }    
					 }    
				 }    
			 };    
			 Thread thread = new Thread(runnable);    
			 thread.start();    
		}
	}
}
