<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ page import="com.util.GETlog" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" href="assets/layui/css/layui.css">
    <link rel="stylesheet" href="assets/common.css"/>
    <script src="${pageContext.request.contextPath}/static/jquery-1.12.1.js"></script>
<title>日志</title>

</head>
<body>
<div class="layui-container">
    <br><br>
    &nbsp;&nbsp;监控日志：
    <div class="layui-btn-group">
        <button class="layui-btn" id="btn-expand1">全部展开</button>
        <button class="layui-btn" id="btn-fold1">全部折叠</button>
    </div>

    &nbsp;&nbsp;
    <input id="edt-search" type="text" placeholder="输入关键字" style="width: 120px;"/>&nbsp;&nbsp;
    <button class="layui-btn" id="btn-search">&nbsp;&nbsp;搜索&nbsp;&nbsp;</button>
    
    <table id="table1" class="layui-table" lay-filter="table1"></table>

</div>

<script src="assets/layui/layui.js"></script>
<script>

	/*update();
	function update()
	{
	
		$.get('${pageContext.request.contextPath}/Servlet_Gao?method=Create_montior_json',function(jdata){
			if(jdata=='')
				return;
		
		})
	}*/
	
    layui.config({
        base: 'module/'
    }).extend({
        treetable: 'treetable-lay/treetable'
    }).use(['table', 'treetable'], function () {
        var $ = layui.jquery;
        var table = layui.table;
        var treetable = layui.treetable;

        // 渲染表格
        var renderTable1 = function () {
            treetable.render({
                treeColIndex: 1,
                treeSpid: -1,
                treeIdName: 'file',
                treePidName: 'pfile',
                treeDefaultClose: true,
                treeLinkage: false,
                elem: '#table1',
                url: '${pageContext.request.contextPath}/Servlet_Gao?method=Create_montior_json',
                page: false,
                cols: [[
                    {type: 'numbers'},
                    {field: 'time', title: '时间'},
                    {field: 'file', title: '文件'},
                    {field: 'Do', title: '操作'},
                    {field: 'info', title: '备注'},
                ]]
            });
        };


        renderTable1();


        $('#btn-expand1').click(function () {
            treetable.expandAll('#table1');
        });

        $('#btn-fold1').click(function () {
            treetable.foldAll('#table1');
        });


        $('#btn-search').click(function () {
            var keyword = $('#edt-search').val();
            var searchCount = 0;
            $('#table1').next('.treeTable').find('.layui-table-body tbody tr td').each(function () {
                $(this).css('background-color', 'transparent');
                var text = $(this).text();
                if (keyword != '' && text.indexOf(keyword) >= 0) {
                    $(this).css('background-color', 'rgba(250,230,160,0.5)');
                    if (searchCount == 0) {
                        treetable.expandAll('#table1');
                        $('html,body').stop(true);
                        $('html,body').animate({scrollTop: $(this).offset().top - 150}, 500);
                    }
                    searchCount++;
                }
            });

            if (keyword == '') {
                layer.msg("请输入搜索内容", {icon: 5});
            } else if (searchCount == 0) {
                layer.msg("没有匹配结果", {icon: 5});
            }
        });
    });
</script>
</body>
</html>