package com.web.tuopu;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.List;

public class EntityToString
{

	/**
	 * @MethodName : getString
	 * @Description : ��ȡ����ȫ�����Լ�����ֵ
	 * @param o
	 *            ��������
	 * @param c
	 *            �����ࡣ���ڻ�ȡ���еķ���
	 * @return
	 */
	public String getStringToShow(Object o, Class< ? > c )
	{
		String result = c.getSimpleName( ) + ":";

		// ��ȡ���ࡣ�ƶ��Ƿ�Ϊʵ����
		if ( c.getSuperclass( ).getName( ).indexOf( "entity" ) >= 0 )
		{
			result +="\n<" +getStringToShow( o , c.getSuperclass( ) )+">,\n";
		}

		// ��ȡ���е�ȫ�������ֶ�
		Field[ ] fields = c.getDeclaredFields( );

		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for ( Field field : fields )
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			field.setAccessible( true );

			try
			{
				// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��

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
		// ��ȡ���е�ȫ�������ֶ�
		Field[ ] fields = c.getDeclaredFields( );
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for ( Field field : fields )
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			field.setAccessible( true );
			try
			{
				// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��
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
	
	//��ȡ�ַ���2��
	public String getString(Object o)
	{
		String result = new String();
		Class<?> c=o.getClass();
		// ��ȡ���е�ȫ�������ֶ�
		Field[ ] fields = c.getDeclaredFields( );
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for ( Field field : fields )
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			field.setAccessible( true );
			try
			{
				// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��
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
	
	//��ȡ�ַ���3��
	public <T> List<String> getStringListSingle(T it)
	{
		List<String> result = new ArrayList<String>();
		Class<?> c=it.getClass();
		// ��ȡ���е�ȫ�������ֶ�
		Field[ ] fields = c.getDeclaredFields( );
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for ( Field field : fields )
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			field.setAccessible( true );
			try
			{
				// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��
				result.add((String)field.get( it ));
			}
			catch ( Exception e )
			{
				// System.out.println("error--------"+methodName+".Reason is:"+e.getMessage());
			}
		}
		return result;
	}
 
	//��ȡT����ϵ���ַ�������2��
	public <T> List<String> getStringList(List<T> o)
	{
		List<String> results=new ArrayList<String>();
		// ��ȡ���е�ȫ�������ֶ�
		Class<?> c=o.get(0).getClass();
		Field[ ] fields = c.getDeclaredFields( );
		for(int i=0;i<o.size();i++)
		{
			String result = new String();
			
			// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
			for ( Field field : fields )
			{
				// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
				field.setAccessible( true );
				try
				{
					// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��
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
	
	
	
	//�����������һϵ��������ֵ������
	public <T> List<String> getStringList(List<T> o,Class<?> c)
	{
		List<String> results=new ArrayList<String>();
		// ��ȡ���е�ȫ�������ֶ�

		Field[ ] fields = c.getDeclaredFields( );
		for(int i=0;i<o.size();i++)
		{
			String result = new String();
			
			// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
			for ( Field field : fields )
			{
				// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
				field.setAccessible( true );
				try
				{
					// �����ֶοɼ����Ϳ�����get������ȡ����ֵ��
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

	//��ö�Ӧ�����б�����ֵ
	public <T> String getNameValue(T it,String name)
	{
		String result=new String();
		Class<?> c=it.getClass();
		// ��ȡ���е�ȫ�������ֶ�
		Field[ ] fields = c.getDeclaredFields( );
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for ( Field field : fields )
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
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
	
	//��ñ����������е�λ��
	public <T> int getNameIndexof(Class<?> c,String name)
	{
		Field[ ] fields = c.getDeclaredFields( );
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for (int i=0;i<fields.length;i++)
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			fields[i].setAccessible( true );
			if(fields[i].getName().equals(name))
				return i;
		}
		return -1;
	}
	
	//������б��������Ƶ�����
	public <T> List<String> getNameList(Class<?> c)
	{
		Field[ ] fields = c.getDeclaredFields( );
		List<String> result=new ArrayList<String>();
		// ѭ�������ֶΣ���ȡ�ֶ���Ӧ������ֵ
		for (int i=0;i<fields.length;i++)
		{
			// ���費Ϊ�ա����ÿɼ��ԣ�Ȼ�󷵻�
			result.add(fields[i].getName());
		}
		return result;
	}
	
	
	
	//������б����ĸ���
	public <T> Integer getNameCount(Class<?> c)
	{
		Field[ ] fields = c.getDeclaredFields( );
		return fields.length;
	}
	
	
	//�������
	public <T> String getClassName(Class<?> c)
	{
		return c.getName();
	}
	
	//���ַ�������Ϊ����ֵ
	@SuppressWarnings("unchecked")
	public <T> T setNameValue(String info,Class<?> in)
	{
		StringHandle sh=new StringHandle();
		return (T) sh.StringListToT(sh.StringNlistToStringList(info.split(" ")), in);
	}

}





