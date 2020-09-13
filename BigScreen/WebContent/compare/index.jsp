<%@page import="com.web.tuopu.FileHandle"%>
<%@page import="com.web.tuopu.Ppyrun"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page language="java" import="java.util.*"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>预测算法对比</title>
<link rel="stylesheet" type="text/css" href="statics/css/style.css" />
</head>
<%
	FileHandle fh=new FileHandle();
	String path=request.getParameter("file");
	
	if(path==null)
	{
		%>
		<center>
			<h1>无预测文件</h1>
		</center>
		<%
		return;
	}
	List<Long> times=new ArrayList<Long>();
	Long past=System.currentTimeMillis();
	List<List<String>> gbdt=Ppyrun.predict_csv(path, 0);
	times.add(System.currentTimeMillis()-past);
	
	past=System.currentTimeMillis();
	List<List<String>> cnn=Ppyrun.predict_csv(path, 2);
	times.add(System.currentTimeMillis()-past);
	
	past=System.currentTimeMillis();
	List<List<String>> brnn=Ppyrun.predict_csv(path, 1);
	times.add(System.currentTimeMillis()-past);
	
	

%>
<body>
<div class="module-line">
	<span class="arrow left-arrow"></span>
	<span class="text">算法对比</span>
	<span class="arrow right-arrow"></span>
</div>

<div class="module-privilege">
	<ul class="privilege-ul name-ul">
		<li class="privilege-item first-item">
			<p class="title">
				<span>算法种类</span>
			</p>
		</li>
		<li class="privilege-item" style="background: #fbf9f8">
			<a>预测花费时间</a>
		</li>
		<li class="privilege-item">
			<a>预测备选根因个数</a>
		</li>
		<li class="privilege-item" style="background: #fbf9f8">
			<a>预测根因</a>
		</li>
		<li class="privilege-item" style="background: #fbf9f8">
			<a>预测根因告警</a>
		</li>
		<li class="privilege-item">
			<a>置信度</a>
		</li>
		<li class="privilege-item" style="background: #fbf9f8">
			<a>备选根因节点</a>
		</li>
		
	</ul>
	<ul class="privilege-ul svip-ul active recommend">
		<li class="privilege-item first-item">
			<div class="svip-type">
				<p class="vip-type-icon">
					<span class="vip-icon svip-middle icon-size-middle"></span>
				</p>
				<span class="vip-type-title">决策树 Histogram算法</span>
			</div>
			<!--<div class="buy-btn-box">
				<p class="center-button-base center-button-light-yellow center-button-container-middle">开通超级会员
				</p>
			</div>-->
		</li>
		<li class="privilege-item" style="background: #fbf4e4"><%=times.get(0)+"ms" %></li>
		<li class="privilege-item"><%=gbdt.size()+"个" %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=gbdt.size()==0?"<span class=\"icon error\"></span>":"node_"+gbdt.get(0).get(1) %></li>
		<li class="privilege-item"><%=gbdt.size()==0?"<span class=\"icon error\"></span>":gbdt.get(0).get(2).substring(0, gbdt.get(0).get(2).length()>30?30:gbdt.get(0).get(2).length()) %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=gbdt.size()==0?"<span class=\"icon error\"></span>":gbdt.get(0).get(4) %></li>
		<li class="privilege-item">
			<%
				if(gbdt.size()>1)
					for(int i=1;i<gbdt.size();i++)
					{
						%>
						node_<%=gbdt.get(i).get(1) %>
						<%
						if(i!=gbdt.size()-1)
						{
							%>
							,
							<%
						}
					}
				else %><span class="icon error"></span><% 
			%>
		</li>
	</ul>
	<ul class="privilege-ul vip-ul ">
		<li class="privilege-item first-item">
			<div class="vip-type">
				<p class="vip-type-icon">
					<span class="vip-icon vip-middle icon-size-middle"></span>
				</p>
				<span class="vip-type-title">CNN</span>
			</div>
			<!--<div class="buy-btn-box">
				<p class="center-button-base center-button-light-red center-button-container-middle">开通会员
				</p>
			</div> -->
		</li>
		<li class="privilege-item" style="background: #fbf4e4"><%=times.get(1)+"ms" %></li>
		<li class="privilege-item"><%=cnn.size()==0?"<span class=\"icon error\"></span>":cnn.size()+"个" %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=cnn.size()==0?"<span class=\"icon error\"></span>":"node_"+cnn.get(0).get(1) %></li>
		<li class="privilege-item"><%=cnn.size()==0?"<span class=\"icon error\"></span>":cnn.get(0).get(2).substring(0, cnn.get(0).get(2).length()>30?30:cnn.get(0).get(2).length()) %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=cnn.size()==0?"<span class=\"icon error\"></span>":cnn.get(0).get(4) %></li>
		<li class="privilege-item">
			<%
				if(cnn.size()>1)
					for(int i=1;i<cnn.size();i++)
					{
						%>
						node_<%=cnn.get(i).get(1) %>
						<%
						if(i!=cnn.size()-1)
						{
							%>
							,
							<%
						}
					}
				else %><span class="icon error"></span><% 
			%>
		</li>
	</ul>
	<ul class="privilege-ul no-vip-ul">
		<li class="privilege-item first-item">
			<div class="no-vip-type">
				<p class="vip-type-icon">
					<span class="vip-icon no-vip-middle icon-size-middle"></span>
				</p>
				<span class="vip-type-title">BRNN</span>
			</div>
		</li>
		<li class="privilege-item" style="background: #fbf4e4"><%=times.get(2)+"ms" %></li>
		<li class="privilege-item"><%=brnn.size()==0?"<span class=\"icon error\"></span>":brnn.size()+"个" %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=brnn.size()==0?"<span class=\"icon error\"></span>":"node_"+brnn.get(0).get(1) %></li>
		<li class="privilege-item"><%=brnn.size()==0?"<span class=\"icon error\"></span>":brnn.get(0).get(2).substring(0, brnn.get(0).get(2).length()>30?30:brnn.get(0).get(2).length()) %></li>
		<li class="privilege-item" style="background: #fbf4e4"><%=brnn.size()==0?"<span class=\"icon error\"></span>":brnn.get(0).get(4) %></li>
		<li class="privilege-item">
			<%
				if(brnn.size()>1)
					for(int i=1;i<brnn.size();i++)
					{
						%>
						node_<%=brnn.get(i).get(1) %>
						<%
						if(i!=brnn.size()-1)
						{
							%>
							,
							<%
						}
					}
				else %><span class="icon error"></span><% 
			%>
		</li>
	</ul>
</div>

<div class="module-line" >
	<span class="arrow left-arrow"></span>
	<span class="text">文件信息</span>
	<span class="arrow right-arrow"></span>
</div>
<center>
	<table border="0" style="font-size:20px">
		<tr>
			<td align="center">文件：</td>
			<td><span style="color:red"><%=path %></span></td>
		</tr>
		<tr>
			<td align="center">预测根因：</td>
			<td><span style="color:red"><%=gbdt.size()==0?"无":"node_"+gbdt.get(0).get(1) %></span></td>
		</tr>
		<tr>
			<td align="center">告警信息：</td>
			<td><span style="color:red"><%=gbdt.size()==0?"无":gbdt.get(0).get(2) %></span></td>
		</tr>
		<tr>
			<td colspan="2">&nbsp;</td>
		</tr>
		<tr>
			<td colspan="2" align="center"><a href="${pageContext.request.contextPath}/static/test/index.html" style="color:lightblue">返回</a> </td>
		</tr>
	</table>
</center>
</body>
</html>