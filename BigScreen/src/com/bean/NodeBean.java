package com.bean;

import java.util.ArrayList;

public class NodeBean {
private String Name_node;
private ArrayList<NodeBean> To_Nodes;
private String Is_toor;
private String Info;

public String getInfo() {
	return Info;
}
public void setInfo(String info) {
	Info = info;
}
public String getName_node() {
	return Name_node;
}
public void setName_node(String name_node) {
	Name_node = name_node;
}
public ArrayList<NodeBean> getTo_Nodes() {
	return To_Nodes;
}
public void setTo_Nodes(ArrayList<NodeBean> to_Nodes) {
	To_Nodes = to_Nodes;
}
public String getIs_toor() {
	return Is_toor;
}
public void setIs_toor(String is_toor) {
	Is_toor = is_toor;
}

}
