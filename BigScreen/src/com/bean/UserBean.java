package com.bean;

import java.util.List;

public class UserBean 
{
	private String Name_sys;
	private String Name_port;
	private String To_sys;
	private String To_port;
	private String Is_root;
	private String Info;
	private String index;
	private List<String> Pre_name_node;
	private List<String> Pre_name_sys;
	private List<String> Be_name_node;
	private List<String> Be_name_sys;
	

	public List<String> getPre_name_node() {
		return Pre_name_node;
	}
	public void setPre_name_node(List<String> pre_name_node) {
		Pre_name_node = pre_name_node;
	}
	public List<String> getPre_name_sys() {
		return Pre_name_sys;
	}
	public void setPre_name_sys(List<String> pre_name_sys) {
		Pre_name_sys = pre_name_sys;
	}
	public List<String> getBe_name_node() {
		return Be_name_node;
	}
	public void setBe_name_node(List<String> be_name_node) {
		Be_name_node = be_name_node;
	}
	public List<String> getBe_name_sys() {
		return Be_name_sys;
	}
	public void setBe_name_sys(List<String> be_name_sys) {
		Be_name_sys = be_name_sys;
	}
	public String getIndex() {
		return index;
	}
	public void setIndex(String index) {
		this.index = index;
	}
	private int Id;
	
	public int getId() {
		return Id;
	}
	public void setId(int id) {
		Id = id;
	}
	public String getIs_root() {
		return Is_root;
	}
	public void setIs_root(String is_root) {
		Is_root = is_root;
	}
	public String getInfo() {
		return Info;
	}
	public void setInfo(String info) {
		Info = info;
	}
	public String getName_sys() {
		return Name_sys;
	}
	public void setName_sys(String name_sys) {
		Name_sys = name_sys;
	}
	public String getName_port() {
		return Name_port;
	}
	public void setName_port(String name_port) {
		Name_port = name_port;
	}

	public String getTo_sys() {
		return To_sys;
	}
	public void setTo_sys(String to_sys) {
		To_sys = to_sys;
	}

	public String getTo_port() {
		return To_port;
	}
	public void setTo_port(String to_port) {
		To_port = to_port;
	}
	
}
