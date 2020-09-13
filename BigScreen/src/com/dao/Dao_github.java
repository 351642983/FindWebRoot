package com.dao;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.json.JSONArray;
import org.json.JSONException;

import com.alibaba.fastjson.JSONObject;
import com.bean.UserBean;
import com.util.DBUtil;
public class Dao_github 
{
	public static void main(String[] args) throws SQLException 
	{
		
		JSONArray array_data=new JSONArray();
		JSONArray array_link=new JSONArray();
		
		//String version=((JSONObject) jsonobject.get(0)).getString("name");
		//System.out.println(version);
		
		ArrayList<UserBean> UserBeans=select_sys();
		ArrayList<UserBean> UserBean_node=select_sys();
		int x=100;
		int y=100;
		int i=0;
		int num_big=0;
		int big_x=100;
		int big_y=100;
		for(UserBean n:UserBeans)
		{
			int num_i=1;
			i=i+1;
			num_big=num_big+1;
	         ArrayList<UserBean> NodeBeans=select_nodes(n.getName_sys());
	         for(UserBean node:NodeBeans)
	         {
	        	 UserBean_node.add(node);
	 			JSONObject job_node = new JSONObject();
	 			node.setId(i);
	 			job_node.put("node_id",i-1);
	 			job_node.put("type", "TEST");
	 			job_node.put("name", node.getName_port());
	 			job_node.put("x",x);
	 			job_node.put("y",y);
	 			job_node.put("fixed",true);
	 			
	 			JSONObject job_node_info = new JSONObject();
	 			job_node_info.put("系统名",n.getName_sys());
	 			job_node_info.put("系统号",num_big);
	 			job_node_info.put("坐标","("+x+","+y+")");
	 			job_node_info.put("I",""+i+"");
	 			job_node_info.put("NUM_I",""+num_i+"");
	 			ArrayList<UserBean> beans=select_info(n.getName_sys(),node.getName_port());
	 			if(beans.size()>0)
	 			{		
	 				job_node_info.put("根因告警信息",beans.get(0).getInfo());
	 			}
	 			job_node.put("info",job_node_info);
	 			big_x=x;
	 			big_y=y;
	 			x=x+300;
	 		
	 			if(num_i%4==0)
	 			{
	 				x=big_x-900;
	 				y=y+300;
	 			}
	 			
	 			i=i+1;
	 			num_i=num_i+1;
		         array_data.put(job_node);
	         }
	         x=100+1500*num_big;
	         if(num_big<4)
	         {
	        	 x=100+1500*num_big;
	        	 y=100;
	         }
	         else
	         {
	        	 x=100+1500*(num_big-6);
	        	 y=1900;
	         }

	         if(num_big==4)
	         {
	        	 x=100;
	        	 y=1000;
	         }
	         if(num_big==5)
	         {
	        	 x=4600;
	        	 y=1000;
	         }
	         if(num_big==6)
	         {
	        	 x=100;
	        	 y=1900;
	         }
	     
		}
		try {
			System.out.println(array_data.get(0));
		} catch (JSONException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		

		ArrayList<UserBean> Nodes_UserBeans=select_node2node();
		String str=array_data.toString();
		for (UserBean n:Nodes_UserBeans)
		{
			
			JSONObject job_sys = new JSONObject();
			int source_id=Get_num_json(str,n.getName_port());
			int target_id=Get_num_json(str,n.getTo_port());
			job_sys.put("source", source_id);
			job_sys.put("target", target_id);
			
			JSONArray array_value=new JSONArray();
			JSONObject job_sys_info = new JSONObject();
			ArrayList<UserBean> beans=select_info_node(n.getTo_port());
			job_sys_info.put("from",n.getName_port());
			job_sys_info.put("to",n.getTo_port());
 			if(beans.size()>0)
 			{		
 				job_sys_info.put("traffic_status","down");
 				job_sys_info.put("根因告警信息",n.getInfo());
 			}
 			else
 			{
 				job_sys_info.put("traffic_status","normal");
 			}
 			array_value.put(job_sys_info);
 			job_sys.put("lines",array_value);
			array_link.put(job_sys);
		}
		
		JSONObject array1=new JSONObject();
		System.out.println(array_data);
		System.out.println(array_link);
		array1.put("nodes",array_data);
		array1.put("relations",array_link);
		System.out.println(array1);
		
		/*
		String num=select_sys_nodes("北京");
		System.out.println(num);
		*/
	}
	

	public static int Get_num_json(String str,String value)
	{
		com.alibaba.fastjson.JSONArray array_data=new com.alibaba.fastjson.JSONArray();
		array_data=JSONObject.parseArray(str);
		for (int i=0;i<array_data.size();i++)
		{
			  JSONObject jsonObject = (JSONObject) array_data.get(i);
			  if(jsonObject.getString("name").equals(value))
			  {
				  return i;
			  }
		}
	      return 0;
	}

	public static ArrayList<UserBean> select_sys_nodes() throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			String sql="select * from sys_and_nodes ";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setName_sys(rs.getString("系统名"));
				userBean.setName_port(rs.getString("系统包括的节点"));
				
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	
	public static ArrayList<UserBean> select_nodes(String sys) throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			String sql="select * from sys_and_nodes where 系统名 = '"+sys+"' ";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setName_port(rs.getString("系统包括的节点"));
				
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	
	
	public static ArrayList<UserBean> select_sys() throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			String sql="select * from sys_and_nodes group by 系统名";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setName_sys(rs.getString("系统名"));
				
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	
	
	public static ArrayList<UserBean> select_sys2sys() throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			String sql="select * from topology_edges_sys ";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setName_sys(rs.getString("源系统"));
				userBean.setTo_sys(rs.getString("目标系统"));
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	
	public static ArrayList<UserBean> select_node2node() throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			String sql="select * from topology_edges_node ";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setName_port(rs.getString("源节点"));
				userBean.setTo_port(rs.getString("目标节点"));
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	public static ArrayList<UserBean> select_info(String sys,String node) throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			
			String sql="select * from train where 系统名称 ='"+sys+"' and 主机='"+node+"' and 根因='1' ";
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setIs_root(rs.getString("根因"));
				userBean.setInfo(rs.getString("告警信息"));
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		
		return userBeans;
	}
	
	public static ArrayList<UserBean> select_info_node(String node) throws SQLException
	{
		Connection conn = DBUtil.getConn();
		ArrayList<UserBean> userBeans=new ArrayList<UserBean>();
		UserBean userBean;
		try {
			Statement state = conn.createStatement();
			
			String sql="select * from train where  主机='"+node+"' and 根因='1' ";
			
			ResultSet rs = state.executeQuery(sql);
			System.out.println(sql);
			while(rs.next()) {
				//如果有结果，是认为是通过验证了
				userBean = new UserBean();
				userBean.setIs_root(rs.getString("根因"));
				userBean.setInfo(rs.getString("告警信息"));
				userBeans.add(userBean);
			}
		} catch (Exception e) 
		{
			e.printStackTrace();
		}
		finally
		{
			conn.close();
		}
		return userBeans;
	}
}
