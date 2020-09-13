package com.bean;

import java.util.ArrayList;

public class SysBean {
private String Name_sys;
private ArrayList<SysBean> To_Sys;
private ArrayList<NodeBean> To_Nodes;
public String getName_sys() {
	return Name_sys;
}
public void setName_sys(String name_sys) {
	Name_sys = name_sys;
}
public ArrayList<SysBean> getTo_Sys() {
	return To_Sys;
}
public void setTo_Sys(ArrayList<SysBean> to_Sys) {
	To_Sys = to_Sys;
}
public ArrayList<NodeBean> getTo_Nodes() {
	return To_Nodes;
}
public void setTo_Nodes(ArrayList<NodeBean> to_Nodes) {
	To_Nodes = to_Nodes;
}

}
