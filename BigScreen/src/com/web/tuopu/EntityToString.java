package com.web.tuopu;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;

public class EntityToString
{

	/**
	 * @MethodName : getString
	 * @Description : 获取类中全部属性及属性值
	 * @param o
	 *            操作对象
	 * @param c
	 *            操作类。用于获取类中的方法
	 * @return
	 */
	public String getStringToShow(Object o, Class< ? > c )
	{
		String result = c.getSimpleName( ) + ":";

		// 获取父类。推断是否为实体类
		if ( c.getSuperclass( ).getName( ).indexOf( "entity" ) >= 0 )
		{
			result +="\n<" +getStringToShow( o , c.getSuperclass( ) )+">,\n";
		}

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

				result += field.getName( ) + "=" + field.get( o ) +",\n";
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		if(result.indexOf( "," )>=0) result = result.substring( 0 , result.length( )-2 );
		return result;
	}

	public String getString(Object o, Class< ? > c )
	{
		String result = new String();
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
				result += field.get( o ) +" ";
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		if(result.length()>=1)
			result = result.substring( 0 , result.length( )-1 );
		return result;
	}
	
	//获取字符串2型
	public String getString(Object o)
	{
		String result = new String();
		Class<?> c=o.getClass();
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
				result += field.get( o ) +" ";
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		if(result.length()>=1)
			result = result.substring( 0 , result.length( )-1 );
		return result;
	}
	
	//获取字符串3形
	public <T> List<String> getStringListSingle(T it)
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
 
	//获取T容器系列字符串容器2型
	public <T> List<String> getStringList(List<T> o)
	{
		List<String> results=new ArrayList<String>();
		// 获取类中的全部定义字段
		Class<?> c=o.get(0).getClass();
		Field[ ] fields = c.getDeclaredFields( );
		for(int i=0;i<o.size();i++)
		{
			String result = new String();
			
			// 循环遍历字段，获取字段相应的属性值
			for ( Field field : fields )
			{
				// 假设不为空。设置可见性，然后返回
				field.setAccessible( true );
				try
				{
					// 设置字段可见，就可以用get方法获取属性值。
					result += field.get( o.get(i) ) +" ";
				}
				catch ( Exception e )
				{
					// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
				}
			}
			if(result.length()>=1)
				result = result.substring( 0 , result.length( )-1 );
			results.add(result);
		}
		return results;
	}
	
	
	
	//获得类容器中一系列容器的值的容器
	public <T> List<String> getStringList(List<T> o,Class<?> c)
	{
		List<String> results=new ArrayList<String>();
		// 获取类中的全部定义字段

		Field[ ] fields = c.getDeclaredFields( );
		for(int i=0;i<o.size();i++)
		{
			String result = new String();
			
			// 循环遍历字段，获取字段相应的属性值
			for ( Field field : fields )
			{
				// 假设不为空。设置可见性，然后返回
				field.setAccessible( true );
				try
				{
					// 设置字段可见，就可以用get方法获取属性值。
					result += field.get( o.get(i) ) +" ";
				}
				catch ( Exception e )
				{
					// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
				}
			}
			if(result.length()>=1)
				result = result.substring( 0 , result.length( )-1 );
			results.add(result);
		}
		return results;
	}

	//获得对应名称中变量的值
	public <T> String getNameValue(T it,String name)
	{
		String result=new String();
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
				if(field.getName().equals(name))
					return (String)field.get( it );
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		return result;
	}
	
	//获得变量名在类中的位置
	public <T> int getNameIndexof(Class<?> c,String name)
	{
		Field[ ] fields = c.getDeclaredFields( );
		// 循环遍历字段，获取字段相应的属性值
		for (int i=0;i<fields.length;i++)
		{
			// 假设不为空。设置可见性，然后返回
			fields[i].setAccessible( true );
			if(fields[i].getName().equals(name))
				return i;
		}
		return -1;
	}
	
	//获得所有变量的名称的容器
	public <T> List<String> getNameList(Class<?> c)
	{
		Field[ ] fields = c.getDeclaredFields( );
		List<String> result=new ArrayList<String>();
		// 循环遍历字段，获取字段相应的属性值
		for (int i=0;i<fields.length;i++)
		{
			// 假设不为空。设置可见性，然后返回
			result.add(fields[i].getName());
		}
		return result;
	}
	
	
	
	//获得所有变量的个数
	public <T> Integer getNameCount(Class<?> c)
	{
		Field[ ] fields = c.getDeclaredFields( );
		return fields.length;
	}
	
	
	//获得类名
	public <T> String getClassName(Class<?> c)
	{
		return c.getName();
	}
	
	//将字符串设置为变量值
	@SuppressWarnings("unchecked")
	public <T> T setNameValue(String info,Class<?> in)
	{
		StringHandle sh=new StringHandle();
		return (T) sh.StringListToT(sh.StringNlistToStringList(info.split(" ")), in);
	}

}





