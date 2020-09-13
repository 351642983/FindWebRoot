package com.web.tuopu;

public class Config {
	//python运行目录
	public static final String workspace="C:/Users/Halo/PycharmProjects/echartsTest";
	//对应的数据目录
	public static final String monthdatadir="C:\\Users\\Halo\\javatest\\BigScreen\\monthdata";
	//监视器监视文件夹
	public static final String checkdir="C:/Users/Halo/Desktop/check";
	//生成日志所在位置
	public static final String checklog="C:\\Users\\Halo\\Desktop\\日志.txt";
	//生成json所在文件夹
	public static final String checklog_json="C:\\Users\\Halo\\javatest\\BigScreen\\WebContent\\CHILD\\表格\\json";
	//默认使用算法种类
	//ptype表示预测所用的算法类型 0表示基于GBDT直方图均衡算法的决策树算法 1表示使用BRNN算法 2表示使用CNN
	public static final Integer ptype=0;
	//监控信息刷新时间
	public static final Integer time_refresh=3000;
	
}
