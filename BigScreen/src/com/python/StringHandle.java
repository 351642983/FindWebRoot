package com.python;

import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class StringHandle {

	
	//返回一个用左字符串，右字符串修饰的字符串
	public String StringAdd(String info,String left,String right)
	{
		return left+info+right;
	}
	
	//用左字符串，右字符串修饰字符串容器
	public List<String> StringListAdd(List<String> infoList,String left,String right)
	{
		int num=infoList.size();
		List<String> ls=new ArrayList<String>();
		for(int i=0;i<num;i++)
		{
			ls.add(left+infoList.get(i)+right);
		}
		return ls;
	}
	
	//将字符串容器组合成一个字符串,并且字符串和字符串之间添加decorate
	public String StringListIntoString(List<String> infoList,String decorate)
	{
		String result=new String();
		int num=infoList.size();
		for(int i=1;i<num;i++)
		{
			result+=decorate+infoList.get(i);
		}
		if(num>0)
			result=infoList.get(0)+result;
		return result;
	}
	
	//将整型容器组合成一个字符串,并且整型和字符串之间添加decorate
	public String IntegerListIntoString(List<Integer> infoList,String decorate)
	{
		String result=new String();
		int num=infoList.size();
		for(int i=1;i<num;i++)
		{
			result+=decorate+infoList.get(i);
		}
		if(num>0)
			result=infoList.get(0)+result;
		return result;
	}
	
	//判断字符串的长度是否处于n到m个长度
	public boolean StringIsSuitLength(String it,int n,int m)
	{
		if(it.length()>=n&&it.length()<=m)
			return true;
		return false;
	}
	
	//判断字符串是否符合正则表达式（全匹配)
	public boolean StringIsSuitExep(String str,String exp)
	{

		boolean isMatch = Pattern.matches(exp, str);
		return isMatch;
	}
	
	//判断字符串是否符合正则表达式（匹配子字符串)
	public boolean StringIsSuitSubExep(String str,String exp)
	{
		// 编译正则表达式
	    Pattern pattern = Pattern.compile(exp);
	    // 忽略大小写的写法
	    // Pattern pat = Pattern.compile(regEx, Pattern.CASE_INSENSITIVE);
	    Matcher matcher = pattern.matcher(str);
	    // 查找字符串中是否有匹配正则表达式的字符/字符串
	    boolean rs = matcher.find();
	    return rs;
	}
	//将Object容器转换为String容器
	public List<String> ObjectListToStringList(List<Object> objList)
	{
		List<String> strList=new ArrayList<String>();
		for(int i=0;i<objList.size();i++)
		{
			strList.add((String)objList.get(i));
		}
		return strList;
	}
	//将Object数组转化为String数组
	public String[] ObjectListToStringNlist(Object []object)
	{
		List<Object> listTemp = java.util.Arrays.asList(object);
		List<String> list=ObjectListToStringList(listTemp);
		String[] strings = new String[list.size()];
		list.toArray(strings);
		return strings;
	}
	//将String容器转换为String数组
	public String[] StringListToStringNlist(List<String> list)
	{
		return list.toArray(new String[list.size()]);
	}
	
	//获得字符串中的符合正则表达式的值
	public List<String> getExpString(String exp,String str)
	{
		Pattern pattern;
		Matcher matcher;
		// 贪婪: 最长匹配 .* : 输出: <biao><>c<b>
		List<String> result=new ArrayList<String>();
		pattern = Pattern.compile(exp);
		matcher = pattern.matcher(str);
		while (matcher.find()) {
			result.add(matcher.group());
		}
		return result;
	}
	
	//获得字符串中的符合正则表达式的值 并去除空白符
	public List<String> getExpStringAndRepalceEmpty(String exp,String str)
	{
		Pattern pattern;
		Matcher matcher;
		// 贪婪: 最长匹配 .* : 输出: <biao><>c<b>
		List<String> result=new ArrayList<String>();
		pattern = Pattern.compile(exp);
		matcher = pattern.matcher(str);
		while (matcher.find()) {
			result.add(matcher.group().replaceAll("\\s", ""));
		}
		return result;
	}
	
	//获得字符串中的符合正则表达式的值 并去除空白符
	public List<String> getExpStringAndRemoveEmpty(String exp,String str)
	{
		Pattern pattern;
		Matcher matcher;
		// 贪婪: 最长匹配 .* : 输出: <biao><>c<b>
		List<String> result=new ArrayList<String>();
		pattern = Pattern.compile(exp);
		matcher = pattern.matcher(str);
		while (matcher.find()) {
			String info=matcher.group();
			if(info==null||StringIsSuitExep(info,"\\s*"))
				continue;
			result.add(info);
		}
		return result;
	}
	
	//获得字符串中的符合正则表达式的值 并去除空白符
	public List<String> getExpStringAndRemoveAndReplaceEmpty(String exp,String str)
	{
		Pattern pattern;
		Matcher matcher;
		// 贪婪: 最长匹配 .* : 输出: <biao><>c<b>
		List<String> result=new ArrayList<String>();
		pattern = Pattern.compile(exp);
		matcher = pattern.matcher(str);
		while (matcher.find()) {
			String info=matcher.group();
			if(info==null||StringIsSuitExep(info,"\\s*"))
				continue;
			result.add(info.replaceAll("\\s", ""));
		}
		return result;
	}
	
	//将Map容器转化为字符串
	public String MapToString(Map<String,String> mapinfos,String insert,String end)
	{
		String result=new String();
		Set<String> s = mapinfos.keySet();//获取KEY集合
		for (String str : s) 
		{
			result+=str+insert+mapinfos.get(str)+end;
		}
		return result;
	}
	
	//将Map容器转化为字符串容器的容器
	public List<List<String>> MapToStringListList(Map<String,String> mapinfos)
	{
		List<List<String>> result=new ArrayList<List<String>>();
		Set<String> s = mapinfos.keySet();//获取KEY集合
		for (String str : s) 
		{
			List<String> lstemp=new ArrayList<String>();
			lstemp.add(str);
			lstemp.add(mapinfos.get(str));
			result.add(lstemp);
		}
		return result;
	}
	
	//将Map<String,Integer>容器转换为Map<String,String>
	public Map<String,String> MapIntegerToMapString(Map<String,Integer> mapinfos)
	{
		Map<String,String> mss=new HashMap<String,String>();
		Set<String> s = mapinfos.keySet();//获取KEY集合
		for (String str : s) 
		{
			mss.put(str, mapinfos.get(str)+"");
		}
		return mss;
		
	}
	
	//去除字符串容器中的空白符
	public List<String> StringListReplaceEmpty(List<String> list)
	{
		List<String> ls=new ArrayList<String>();
		int num=list.size();
		for(int i=0;i<num;i++)
		{
			String info=list.get(i);
			if(info!=null)
				ls.add(info.replaceAll("\\s", ""));
			else ls.add(info);
		}
		return ls;
	}
	
	//移除字符串容器中的空白符字符串
	public List<String> StringListRemoveEmpty(List<String> list)
	{
		List<String> ls=new ArrayList<String>();
		int num=list.size();
		for(int i=0;i<num;i++)
		{
			String info=list.get(i);
			if(info==null||StringIsSuitExep(info,"\\s*"))
				continue;
			//System.out.println(StringIsSuitExep(info,"\\s*")+"  字符串:\""+info+"\"");
			ls.add(info);
		}
		return ls;
	}
	//移除字符串容器中的空白符字符串并将空白字符替换为空
	public List<String> StringListRemoveAndReplaceEmpty(List<String> list)
	{
		List<String> ls=new ArrayList<String>();
		int num=list.size();
		for(int i=0;i<num;i++)
		{
			String info=list.get(i);
			if(info==null||StringIsSuitExep(info,"\\s*"))
				continue;
			//System.out.println(StringIsSuitExep(info,"\\s*")+"  字符串:\""+info+"\"");
			ls.add(info.replaceAll("\\s", ""));
		}
		return ls;
	}
	
	
	//将String数组转换为String容器
	public List<String> StringNlistToStringList(String []strlist)
	{
		List<String> list = java.util.Arrays.asList(strlist);
		return list;
	}
	
	//判断一系列的以空格分开的字符串序列中的特定位置是否含有相对应的信息(全一致长度容器),有的话返回对应行数容器，没有的话返回null
	public List<Integer> judgeStringListContainPerfect(List<List<String>> info,int count,String contain)
	{
		List<Integer> numList=new ArrayList<Integer>();
		int g_size=info.size();
		for(int i=0;i<g_size;i++)
		{
			int g_initsize=info.get(i).size();
			if(g_initsize>count)
			{
				return null;
			}
			else
			{
				if(!info.get(i).get(count-1).equals(contain))
				{
					continue;
				}
				else
				{
					numList.add(i);
				}
				
			}
		}
		if(numList.size()==0)
			return null;
		else return numList;
	}
	
	
	//将字符串中符合正则表达式的字符替换为空
	public List<String> StringListReplaceAll(List<String> infos,String exp)
	{
		List<String> result=new ArrayList<String>();
		int g_size=infos.size();
		for(int i=0;i<g_size;i++)
		{
			String temp=infos.get(i).replaceAll(exp, "");
			result.add(temp);
		}
		return result;
	}
	
	//判断一系列的以空格分开的字符串序列中的特定位置是否含有相对应的信息(非全一致长度容器),有的话返回对应行数容器，没有的话返回null
	public List<Integer> judgeStringListContain(List<List<String>> info,int count,String contain)
	{
		List<Integer> numList=new ArrayList<Integer>();
		int g_size=info.size();
		for(int i=0;i<g_size;i++)
		{
			int g_initsize=info.get(i).size();
			if(g_initsize>count)
			{
				continue;
			}
			else
			{
				if(!info.get(i).get(count-1).equals(contain))
				{
					continue;
				}
				else
				{
					numList.add(i);
				}
				
			}
		}
		if(numList.size()==0)
			return null;
		else return numList;
	}
	
	//以对应正则表达式分隔字符并且将分隔后的字符串储存进字符串容器中
	public List<List<String>> StringSplitByExpToStringList(List<String> strlist,String exp)
	{
		List<List<String>> strresult=new ArrayList<List<String>>();
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			String list=strlist.get(i);
			if(list==null||list.equals(""))
			{
				strresult.add(StringNlistToStringList(new String[]{"",""}));
				continue;
			}
			String []strnlist=list.split(exp);
			strresult.add(StringNlistToStringList(strnlist));
		}
		return strresult;
	}
	
	//以对应正则表达式分隔字符并且将分隔后的字符串储存进类容器中
	public <T> List<T> StringSplitByExpToTList(List<String> strlist,String exp,String []namelist,Class<T> clazz)
	{
		List<T> tresult=new ArrayList<T>();
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			String list=strlist.get(i);
			if(list==null||list.equals(""))
				continue;
			String []nlist=list.split(exp);
			if(nlist.length<namelist.length)
			{
				throw new IllegalArgumentException("The Length of namelist is longer than nlist");
			}
			T bean;
			try {
				bean = clazz.newInstance();
				int num=namelist.length;
				for(int j=0;j<num;j++)
				{
					Field fs=getDeclaredField(bean, namelist[j]);
					if(fs==null){
						throw new IllegalArgumentException("Could not find field["+ 
								namelist[j]+"] on target ["+bean+"]");
					}
					makeAccessiable(fs);
				    try{
				        fs.set(bean, (Object)nlist[j]);
				    }
				    catch(IllegalAccessException e){
				        System.out.println("不可能抛出的异常");
				    }
					
				}
				tresult.add(bean);
			} catch (InstantiationException | IllegalAccessException e1) {
				// TODO 自动生成的 catch 块
				e1.printStackTrace();
			}
			
		}
		return tresult;
	}
	
	//以对应正则表达式分隔字符并且将分隔后的字符串储存进类容器中(自动型)
	public <T> List<T> StringSplitByExpToTList(List<String> strlist,String exp,Class<T> clazz)
	{
		List<T> tresult=new ArrayList<T>();
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			String list=strlist.get(i);
			if(list==null||list.equals(""))
				continue;
			String []nlist=list.split(exp);

			Field[ ] fields = clazz.getDeclaredFields( );

			T bean;
			try {
				bean = clazz.newInstance();
				// 循环遍历字段，获取字段相应的属性值
				int j=0;
				for ( Field field : fields )
				{
					// 假设不为空。设置可见性，然后返回
					field.setAccessible( true );
					try
					{
						Field fs=getDeclaredField(bean, field.getName( ));
						if(fs==null){
							throw new IllegalArgumentException("Could not find field["+ 
									field.getName( )+"] on target ["+bean+"]");
						}
						makeAccessiable(fs);
						try{
							fs.set(bean, (Object)nlist[j]);
						}
						catch(IllegalAccessException e){
							System.out.println("不可能抛出的异常");
						}
						// 设置字段可见，就可以用get方法获取属性值。
						//result += field.get( o ) +" ";
						++j;
					}
					catch ( Exception e )
					{
						// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
					}
				}



				tresult.add(bean);
			} catch (InstantiationException | IllegalAccessException e1) {
				// TODO 自动生成的 catch 块
				e1.printStackTrace();
			}

		}
		return tresult;
	}
	
	//将字符串容器的容器组合成一个字符串容器,并且字符串和字符串之间添加decorate
	public List<String> StringListListIntoStringList(List<List<String>> infoList,String decorate)
	{
		List<String> result=new ArrayList<String>();
		int num=infoList.size();
		for(int i=0;i<num;i++)
		{
			int initnum=infoList.get(i).size();
			String resultTemp=new String();
			for(int j=1;j<initnum;j++)
			{
				resultTemp+=decorate+infoList.get(i).get(j);
			}
			if(initnum>0)
				resultTemp=infoList.get(i).get(0)+resultTemp;
			result.add(resultTemp);
		}
		return result;
	}
	//删除string容器中符合正则表达式的元素
	public List<String> deleteStringListIsSuitExp(List<String> strlist,String exp)
	{
		Iterator<String> it = strlist.iterator();
		while(it.hasNext()){
			String x = it.next();
			if(StringIsSuitExep(x, exp)){
				it.remove();
			}
		}
		return strlist;
	}
	//删除string容器的容器中符合正则表达式的元素
	public List<List<String>> deleteStringListListIsSuitExp(List<List<String>> strlist,String exp)
	{
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			List<String> itTemp=new ArrayList<String>(strlist.get(i));
			Iterator<String> it = itTemp.iterator();
			while(it.hasNext()){
				if(StringIsSuitExep(it.next(), exp)){
					it.remove();
				}
			}
			strlist.set(i, itTemp);
		}
		return strlist;
	}
	
	//将字符串容器的容器拼接成字符串容器
	public List<String> StringListListAddToStringList(List<List<String>> strllist)
	{
		List<String> strResult=new ArrayList<String>();
		Integer g_size=strllist.size();
		for(int i=0;i<g_size;i++)
		{
			strResult.addAll(strllist.get(i));
		}
		return strResult;
	}
	
	//将字符串容器的值统计并记录进Map中
	public Map<String,Integer> StringListToMapValue(List<String> strlist)
	{
		Map<String,Integer> maplist=new HashMap<String,Integer>();
		Integer g_size=strlist.size();
		for(int i=0;i<g_size;i++) {

			Integer g_map=maplist.get(strlist.get(i));
			if(g_map==null)
			{
				maplist.put(strlist.get(i),1);
			}
			else
			{
				maplist.put(strlist.get(i), g_map+1);
			}
		}
		return maplist;
	}
	
	//将两个字符串容器对应链接成Map
	public Map<String,String> StringListToMap(List<String> list1,List<String> list2)
	{
		Map<String,String> map=new HashMap<String,String>();
		int g_size=list1.size();
		if(list1.size()!=list2.size())
			return map;
		else
		{
			for(int i=0;i<g_size;i++)
			{
				map.put(list1.get(i), list2.get(i));
			}
		}
		return map;
	}
	
	//将字符串容器和整型容器对应链接成Map
	public Map<String,Integer> StringListAndIntegerListToMap(List<String> list1,List<Integer> list2)
	{
		Map<String,Integer> map=new HashMap<String,Integer>();
		int g_size=list1.size();
		if(list1.size()!=list2.size())
			return map;
		else
		{
			for(int i=0;i<g_size;i++)
			{
				map.put(list1.get(i), list2.get(i));
			}
		}
		return map;
	}
	
	
	
	
	//抽取字符串容器容器中的某一列出来(perfect型)
	public List<String> StringListListInitSingleList(List<List<String>> strlist,Integer index)
	{
		List<String> strlistTemp=new ArrayList<String>();
		int g_size=strlist.size();
		if(g_size==0)
			return strlistTemp;
		if(index>=strlist.get(0).size())
			return strlistTemp;
		for(int i=0;i<g_size;i++)
		{
			strlistTemp.add(strlist.get(i).get(index));
		}
		return strlistTemp;
	}
	
	
	
	//字符串列表精确包含某个字符串
	public boolean StringListIsExContainString(List<String> strlist,String it)
	{
		int num=strlist.size();
		for(int i=0;i<num;i++)
		{
			if(strlist.get(i).equals(it))
				return true;
		}
		return false;
	}
	//字符串列表包含某个字符串
	public boolean StringListIsContainString(List<String> strlist,String it)
	{
		int num=strlist.size();
		for(int i=0;i<num;i++)
		{
			if(strlist.get(i).contains(it))
				return true;
		}
		return false;
	}
	
	//字符串列表包含某个字符串
	public boolean StringIsContainStringList(String it,List<String> strlist)
	{
		int num=strlist.size();
		for(int i=0;i<num;i++)
		{
			if(it.contains(strlist.get(i)))
				return true;
		}
		return false;
	}

	//字符串容器和字符串容器中将互相包含的元素取出
	public List<String> StringListSameOutStringList(List<String> strlist1,List<String> strlist2)
	{
		List<String> result=new ArrayList<String>();
		int g_size=strlist1.size();
		int g_size2=strlist2.size();
		if(g_size==0||g_size2==0)
			return result;
		for(int i=0;i<g_size;i++)
		{
			String itTemp=strlist1.get(i);
			if(StringListIsExContainString(strlist2,itTemp))
			{
				result.add(itTemp);
			}
		}
		return result;
	}
	
	//字符串容器和字符串容器中相似的元素取出
	public List<String> StringListLikeOutStringList(List<String> strlist1,List<String> strlist2)
	{
		List<String> result=new ArrayList<String>();
		int g_size=strlist1.size();
		int g_size2=strlist2.size();
		if(g_size==0||g_size2==0)
			return result;
		for(int i=0;i<g_size;i++)
		{
			String itTemp=strlist1.get(i);
			if(StringIsContainStringList(itTemp,strlist2))
			{
				result.add(itTemp);
			}
		}
		return result;
	}
	//字符串容器和字符串中相似的元素取出序号
	public List<Integer> StringLikeOutStringListId(List<String> strlist1,String strlist2)
	{
		List<Integer> result=new ArrayList<Integer>();
		int g_size=strlist1.size();
		if(g_size==0)
			return result;
		for(int i=0;i<g_size;i++)
		{
			String itTemp=strlist1.get(i);
			if(itTemp.contains(strlist2))
			{
				result.add(i);
			}
		}
		return result;
	}
	//将字符串中重复的元素移除
	public List<String> StringListRemoveRepeat(List<String> infos)
	{
		List<String> result=new ArrayList<String>();
		int g_size=infos.size();
		for(int i=0;i<g_size;i++)
		{
			String temp=infos.get(i);
			if(!StringListContainString(result,temp))
			{
				result.add(temp);
			}
		}
		return result;
	}
	
	//判断字符串中是否含有
	public boolean StringListContainString(List<String> info,String txt)
	{
		int g_size=info.size();
		for(int i=0;i<g_size;i++)
		{
			if(info.get(i).equals(txt))
			{
				return true;
			}
		}
		return false;
	}
	
	
	//返回对应子字符串容器中对应字符串中的位置的容器
	public List<Integer> StringListInStringListIndexof(List<String> allinfo,List<String> sublist)
	{
		List<Integer> numlist=new ArrayList<Integer>();
		int g_size=allinfo.size();
		int g_size2=sublist.size();
		if(g_size==0||g_size2==0)
			return numlist;
		for(int i=0;i<g_size2;i++)
		{
			numlist.add(allinfo.indexOf(sublist.get(i)));
		}
		return numlist;
	}
	
	//返回对应子字符串容器中对应字符串中的位置的容器
	public List<Integer> StringInStringListIndexofAll(List<String> allinfo,String str)
	{
		List<Integer> numlist=new ArrayList<Integer>();
		int g_size=allinfo.size();
		if(g_size==0)
			return numlist;
		for(int i=0;i<g_size;i++)
		{
			if(allinfo.get(i).equals(str))
				numlist.add(i);
		}
		return numlist;
	}
	
	//将数值的容器转换的字符串容器
	public List<String> IntegerListIntoStringList(List<Integer> li)
	{
		List<String> ls=new ArrayList<String>();
		int max=li.size();
		for(int i=0;i<max;i++)
		{
			ls.add(li.get(i)+"");
		}
		return ls;
	}
	
	//字符串添加字符串容器到字符串容器的容器
	public List<List<String>> StringListAddStringList(List<String> list1,List<String> list2)
	{
		List<List<String>> lls=new ArrayList<List<String>>();
		int max=list1.size();
		for(int i=0;i<max;i++)
		{
			List<String> init=new ArrayList<String>();
			init.add(list1.get(i));
			init.add(list2.get(i));
			lls.add(init);
		}
		return lls;
	}
	
	
	
	//将字符串容器的容器转换为T容器
	public <T> List<T> StringListListToTlist(List<List<String>> strlist,Class<?> clazz)
	{
		List<T> tresult=new ArrayList<T>();
		int g_size=strlist.size();
		Field[ ] fields = clazz.getDeclaredFields( );
		for(int i=0;i<g_size;i++)
		{
			List<String> list=strlist.get(i);
			if(list==null)
				continue;
			String []nlist=StringListToStringNlist(list);

			T bean;
			try {
				bean = (T) clazz.newInstance();
				// 循环遍历字段，获取字段相应的属性值
				int j=0;
				for ( Field field : fields )
				{
					// 假设不为空。设置可见性，然后返回
					field.setAccessible( true );
					try
					{
						Field fs=getDeclaredField(bean, field.getName( ));
						if(fs==null){
							throw new IllegalArgumentException("Could not find field["+ 
									field.getName( )+"] on target ["+bean+"]");
						}
						makeAccessiable(fs);
						try{
							fs.set(bean, (Object)nlist[j]);
						}
						catch(IllegalAccessException e){
							System.out.println("不可能抛出的异常");
						}
						// 设置字段可见，就可以用get方法获取属性值。
						//result += field.get( o ) +" ";
						++j;
					}
					catch ( Exception e )
					{
						// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
					}
				}



				tresult.add(bean);
			} catch (InstantiationException | IllegalAccessException e1) {
				// TODO 自动生成的 catch 块
				e1.printStackTrace();
			}

		}
		return tresult;
	}
	
	//将字符串容器的容器中取出对应整型容器对应位置的字符串的容器的容器
	public List<List<String>> StringListListInitIndexOfIntegerList(List<List<String>> ls,List<Integer> indexof)
	{
		int g_size=ls.size();
		System.out.println(g_size);
		int g_numsize=indexof.size();
		List<List<String>> result=new ArrayList<List<String>>();
		for(int i=0;i<g_size;i++)
		{
			List<String> temp=new ArrayList<String>();

			for(int j=0;j<g_numsize;j++)
			{
				temp.add(ls.get(i).get(indexof.get(j)));
			}
			
			result.add(temp);
		}
		return result;
	}
	//将字符串容器的容器中取出对应整型容器对应位置的字符串的容器的容器
	public List<List<String>> StringListListInitIndexOfIntegerListRows(List<List<String>> ls,List<Integer> indexof)
	{
		int g_size=ls.size();
		System.out.println(g_size);
		int g_numsize=indexof.size();
		List<List<String>> result=new ArrayList<List<String>>();

		for(int j=0;j<g_numsize;j++)
		{
			result.add(ls.get(indexof.get(j)));
		}
			
		return result;
	}
	
	
	//将字符串容器的容器链接上对应字符串容器的容器
	public List<List<String>> StringListListAddToByStringListList(List<List<String>> strlistlist,List<List<String>> strlist)
	{
		int g_size=strlistlist.size();
		List<List<String>> result=new ArrayList<List<String>>();
		for(int i=0;i<g_size;i++)
		{
			List<String> strTemp=new ArrayList<String>(strlistlist.get(i));
			strTemp.addAll(strlist.get(i));
			result.add(strTemp);
		}
		return result;
	}
	
	
	//将对应的T容器转换为字符串的容器的容器
	public <T> List<List<String>> TListToStringListList(List<T> tlist)
	{
		List<List<String>> result=new ArrayList<List<String>>();
		int g_size=tlist.size();
		if(g_size==0)
			return result;
		EntityToString ets=new EntityToString();
		for(int i=0;i<g_size;i++)
		{
			result.add(StringNlistToStringList(ets.getString(tlist.get(i), tlist.get(i).getClass()).split(" ")));
		}
		return result;
	
	}
	
	//返回字符串容器中符合正则的字符串容器
	public List<String> StringListGetSuitExpStringList(List<String> strlist,String exp)
	{
		List<String> temp=new ArrayList<String>();
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			String subtemp=strlist.get(i);
			if(StringIsSuitExep(subtemp,exp))
				temp.add(subtemp);
		}
		return temp;
	}
	
	//返回字符串容器中字符包含符合正则的字符串容器
	public List<String> StringListGetSuitSubExpStringList(List<String> strlist,String subexp)
	{
		List<String> temp=new ArrayList<String>();
		int g_size=strlist.size();
		for(int i=0;i<g_size;i++)
		{
			String subtemp=strlist.get(i);
			if(StringIsSuitSubExep(subtemp,subexp))
				temp.add(subtemp);
		}
		return temp;
	}
	
	
	
	//获得对应类容器中的字符串容器
	public <T> List<String> getTSingleList(List<T> tlist,String name)
	{
		StringHandle sh=new StringHandle();
		EntityToString ets=new EntityToString();
		return sh.StringListListInitSingleList(sh.TListToStringListList(tlist), ets.getNameIndexof(tlist.get(0).getClass(), name));
	}
	
	//将T转换为字符串容器
	public <T> List<String> TToStringList(T it)
	{
		List<String> result = new ArrayList<String>();
		Class<?> c=it.getClass();
		// 获取类中的全部定义字段
		Field[ ] fields = c.getDeclaredFields( );
		// 循环遍历字段，获取字段相应的属性值
		for ( Field field : fields )
		{
			// 假设不为空。设置可见性，然后返回
			field.setAccessible( true );
			try
			{
				// 设置字段可见，就可以用get方法获取属性值。
				result.add((String)field.get( it ));
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		return result;
	}
	//将字符串容器的容器链接上对应字符串容器
	public List<List<String>> StringListListAddToStringListList(List<List<String>> strlistlist,List<String> strlist)
	{
		int g_size=strlistlist.size();
		List<List<String>> result=new ArrayList<List<String>>();
		for(int i=0;i<g_size;i++)
		{
			List<String> strTemp=new ArrayList<String>(strlistlist.get(i));
			strTemp.add(strlist.get(i));
			result.add(strTemp);
		}
		return result;
	}
	
	//将字符串容器的值转换为T
	public <T> T StringListToT(List<String> it,Class<T> clazz)
	{

		Field[ ] fields = clazz.getDeclaredFields( );
		T bean=null;
		try {
			bean=(T) clazz.newInstance();
			// 循环遍历字段，获取字段相应的属性值
			int j=0;
			for ( Field field : fields )
			{
				// 假设不为空。设置可见性，然后返回
				field.setAccessible( true );
				try
				{
					Field fs=getDeclaredField(bean, field.getName( ));
					if(fs==null){
						throw new IllegalArgumentException("Could not find field["+ 
								field.getName( )+"] on target ["+bean+"]");
					}
					makeAccessiable(fs);
					try{
						fs.set(bean, (Object)it.get(j));
					}
					catch(IllegalAccessException e){
						System.out.println("不可能抛出的异常");
					}
					// 设置字段可见，就可以用get方法获取属性值。
					//result += field.get( o ) +" ";
					++j;
				}
				catch ( Exception e )
				{
					// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
				}
			}
		} catch (InstantiationException | IllegalAccessException e1) {
			// TODO 自动生成的 catch 块
			e1.printStackTrace();
		}
		return bean;
	}
	//将字符串转换成T类
	public <T> T StringToT(String str,Class<T> it)
	{
		return StringListToT(StringNlistToStringList(str.split(" ")),it);
	}

	//获取field属性，属性有可能在父类中继承 
	public Field getDeclaredField(Object obj,String fieldName){
		for (Class<?> clazz=obj.getClass(); clazz!=Object.class; clazz=clazz.getSuperclass()){
			try{
				return clazz.getDeclaredField(fieldName);
			}
			catch(Exception e){
			}
		}
		return null;
	}
	


	//判断field的修饰符是否是public,并据此改变field的访问权限 
	public void makeAccessiable(Field field){
		if(!Modifier.isPublic(field.getModifiers())){
			field.setAccessible(true);
		}
	}
	
	
}
