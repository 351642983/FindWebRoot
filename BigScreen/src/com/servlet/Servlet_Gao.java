package com.servlet;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.json.JSONArray;

import com.python.Ppyrun;
import com.python.Ppyrun_pre;
import com.web.tuopu.Config;
import com.web.tuopu.DataServlet;

/**
 * Servlet implementation class Servlet_Gao
 */
@WebServlet("/Servlet_Gao")
public class Servlet_Gao extends HttpServlet {
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// TODO Auto-generated method stub
		req.setCharacterEncoding("utf-8");
		String method = req.getParameter("method");
//		System.out.println("PPPPPPPPPPPPPPP");
		if ("Time_qunee".equals(method)) {
			try {
				Time_qunee(req, resp);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if ("Time_qunee_pre".equals(method)) {
			try {
				Time_qunee_pre(req, resp);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if ("Time_qunee_fold".equals(method)) {
			try {
				Time_qunee_fold(req, resp);
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
		else if("Create_root_json".equals(method)) {
			resp.setCharacterEncoding("utf-8");
			resp.getWriter().write(DataServlet.createRootInfoJson());
		}
		else if("Create_montior_json".equals(method)) {
			resp.setCharacterEncoding("utf-8");
			resp.getWriter().write(DataServlet.createMontiorInfoJson());
		}
	}
    public Servlet_Gao() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
    private void Time_qunee(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException, SQLException {
  		// TODO Auto-generated method stub
  		//response.getWriter().append("Served at: ").append(request.getContextPath());
  		req.setCharacterEncoding("utf-8");
  		resp.setContentType("text/html;charset=utf-8");
  		HttpSession session=req.getSession();
  		PrintWriter out=resp.getWriter();
  		String Filename = req.getParameter("Filename");
  		JSONArray array_data=Ppyrun.GET_file_json(Filename);
         
		resp.setCharacterEncoding("UTF-8");
		System.out.println(array_data.toString());
  		//resp.sendRedirect(req.getContextPath() + "/admin/child/Child_11/1_Rcai.jsp");
		resp.getWriter().write(array_data.toString());
  		}
    private void Time_qunee_pre(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException, SQLException {
  		// TODO Auto-generated method stub
  		//response.getWriter().append("Served at: ").append(request.getContextPath());
  		req.setCharacterEncoding("utf-8");
  		resp.setContentType("text/html;charset=utf-8");
  		HttpSession session=req.getSession();
  		PrintWriter out=resp.getWriter();
  		String Filename = req.getParameter("Filename");
  		
  		String Nodename = Ppyrun.GET_NAME(Filename) ;
  		
  		JSONArray array_data=Ppyrun.GET_file_json(Filename);
  		
  		JSONArray array_data_pre=Ppyrun_pre.GET_Value_json(Filename,Nodename);
  		JSONArray array1=new JSONArray();
  		array1.put(array_data);
		array1.put(array_data_pre);
		resp.setCharacterEncoding("UTF-8");
		System.out.println(array1.toString());
  		//resp.sendRedirect(req.getContextPath() + "/admin/child/Child_11/1_Rcai.jsp");
		resp.getWriter().write(array1.toString());
  		}
    private void Time_qunee_fold(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException, SQLException {
  		// TODO Auto-generated method stub
  		//response.getWriter().append("Served at: ").append(request.getContextPath());
  		req.setCharacterEncoding("utf-8");
  		resp.setContentType("text/html;charset=utf-8");
  		HttpSession session=req.getSession();
  		PrintWriter out=resp.getWriter();
  		String Foldname = req.getParameter("Foldname");
  		JSONArray array_data=Ppyrun.GET_waring_json(Foldname);
         
		resp.setCharacterEncoding("UTF-8");
		System.out.println(array_data.toString());
  		//resp.sendRedirect(req.getContextPath() + "/admin/child/Child_11/1_Rcai.jsp");
		resp.getWriter().write(array_data.toString());
  		}
}
