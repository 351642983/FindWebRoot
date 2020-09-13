package com.dao;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;

import org.json.JSONArray;
import org.json.JSONException;

import com.alibaba.fastjson.JSONObject;
import com.bean.UserBean;
import com.util.DBUtil;

public class DDAO {
	public static void main(String[] args) throws SQLException 
	{
		
		JSONArray array_data=new JSONArray();
		JSONArray array_link=new JSONArray();
		JSONArray array1=new JSONArray();
		String img_sys="data-1547632686885-o5Rfi3tyk.png";
		String img_node="data-1547632915872-WZMUphq72.png";
		int y=100;
		int x=15;

		ArrayList<UserBean> UserBeans=select_sys();
		int i=0;
		for(UserBean n:UserBeans)
		{
			
			JSONObject job_sys = new JSONObject();
			job_sys.put("name", n.getName_sys());
			job_sys.put("img", img_sys);
			job_sys.put("alarm", "告警");
			job_sys.put("symbolSize", "35");
			job_sys.put("x", ""+x);
			job_sys.put("y", ""+y);
			
	 		int node_y=y+20-10;
			int node_x=x-15+10;
	         ArrayList<UserBean> NodeBeans=select_nodes(n.getName_sys());
	         for(UserBean node:NodeBeans)
	         {
	 			JSONObject job_node = new JSONObject();
	 			job_node.put("name", node.getName_port());
	 			job_node.put("img", img_node);
	 			job_node.put("alarm", "告警");
	 			job_node.put("symbolSize", "20");
	 			job_node.put("x", ""+node_x);
	 			job_node.put("y", ""+node_y);
	 		
	 			node_x=node_x+10;
		
	 			if(node_x>x+15-10)
				{
		 			node_y=node_y-10;
		 			node_x=x-15+10;
				}
		         array_data.put(job_node);
	         }
			
			if(i%2==0)
			{
				x=x+30;
			}
			else
			{
				x=x+90;
			}
			
			if(x>105)
			{
				i=i+1;
				y=y-40;
				x=15;
			}
	         array_data.put(job_sys);

		}
		UserBeans=select_sys2sys();
		for (UserBean n:UserBeans)
		{
			JSONObject job_sys = new JSONObject();
			job_sys.put("source", n.getName_sys());
			job_sys.put("target", n.getTo_sys());
			job_sys.put("name", "数据传输");
			array_link.put(job_sys);
		}

		
		UserBeans=select_sys_nodes();
		for (UserBean n:UserBeans)
		{
			JSONObject job_sys = new JSONObject();
			job_sys.put("target", n.getName_sys());
			job_sys.put("source", n.getName_port());
			job_sys.put("name", "数据传输");
			array_link.put(job_sys);
		}
		
		
		array1.put(array_data);
		array1.put(array_link);
		
		try {
			System.out.println(array1.get(0));
			System.out.println(array1.get(1));
		} catch (JSONException e) {
			// TODO 自动生成的 catch 块
			e.printStackTrace();
		}
		
		/*
		String num=select_sys_nodes("北京");
		System.out.println(num);
		*/
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
			String sql="select * from train where 系统名称 ='"+sys+"' and 主机='"+node+"' ";
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
}
