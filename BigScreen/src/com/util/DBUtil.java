package com.util;

import java.sql.*;

/**
 * ���ݿ�Ĺ�����
 * @author zm
 *
 */
public class DBUtil {
	//eshopΪ���ݿ����ƣ�db_userΪ���ݿ��û���db_passwordΪ���ݿ�����
public static String db_url ="jdbc:mysql://localhost:3306/soft_tuopu?&useSSL=false&serverTimezone=UTC";
	public static String db_user = "root";
	public static String db_password = "zb753951";

	public static Connection getConn() {
		Connection conn = null;
		try {
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection(db_url, db_user, db_password);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}
	
	public static void close(Statement state, Connection conn) {
		if(state!=null) {
			try {
				state.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if(conn!=null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void close(ResultSet rs, Statement state, Connection conn) {
		if(rs!=null) {
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if(state!=null) {
			try {
				state.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if(conn!=null) {
			try {
				conn.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
	}
}
