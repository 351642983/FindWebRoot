<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>网络实时拓扑结构可视化系统</title>
</head>
<body>
<div style="position: absolute; width: 100%; top: 0px; bottom: 0px;" id="canvas"></div>
<script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/lib/qunee-min.js?v=2.7.7.5"></script>
<script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/common.js?v=2.7.7.5"></script>
<script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/graphs.js?v=2.7.7.5"></script>
<script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/demo.js?v=2.7.7.5"></script> 
<script src="${pageContext.request.contextPath}/static/jquery-1.12.1.js"></script>

<link rel="stylesheet" href="${pageContext.request.contextPath}/static/qunee/js/codemirror/codemirror.css">
<script src="${pageContext.request.contextPath}/static/qunee/js/codemirror/codemirror.js?v=2.7.7.5"></script>
<script src="${pageContext.request.contextPath}/static/qunee/js/codemirror/javascript.js?v=2.7.7.5"></script>

    <link rel="stylesheet" href="${pageContext.request.contextPath}/static/qunee/js/bootstrap/bootstrap.min.css"/>
    <link rel="stylesheet" href="${pageContext.request.contextPath}/static/qunee/demo.css?v=2.6"/>
    <script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/i18n.js?v=2.7.7.5"></script>
    <script type="text/javascript" src="./${pageContext.request.contextPath}/static/qunee/js/check-IE678.js?v=2.7.7.5"></script>

    <script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/jquery/jquery.min.js?v=2.7.7.5"></script>
    <script type="text/javascript" src="${pageContext.request.contextPath}/static/qunee/js/bootstrap/bootstrap.min.js?v=2.7.7.5"></script>
<%
 String Foldname=request.getParameter("Foldname");
//String Foldname="E:\\pycharm\\WorkPlace\\FINAL_TUO\\test";
%>
<script>
    var graph = new Q.Graph('canvas');
    graph.zoomToOverview();
    graph.styles = {};
    graph.styles[Q.Styles.LABEL_FONT_SIZE] = 18;
    createText(getI18NString('拓扑结构实时可视化系统'), 2800, 1300, 300, "#F00");

    var group1 = createGroup(50);
   	createText(getI18NString('SYS1'), 550,400,200, "#F00", group1);
    var group2 = createGroup(50);
  	createText(getI18NString('SYS2'), 2050,400,200, "#F00", group2);
    var group3 = createGroup(50);
	createText(getI18NString('SYS3'), 3550,400,200, "#F00", group3);
    var group4 = createGroup(50);
	createText(getI18NString('SYS4'), 5050,400,200, "#F00", group4);
    var group5 = createGroup(50);
    createText(getI18NString('SYS5'), 550,1300,200, "#F00", group5);
    var group6 = createGroup(50);
    createText(getI18NString('SYS6'), 5050,1300,200, "#F00", group6);
    var group7 = createGroup(50);
    createText(getI18NString('SYS7'), 550,2000,200, "#F00", group7);
    var group8 = createGroup(50);
    createText(getI18NString('SYS8'), 2050,2200,200, "#F00", group8);
    var group9 = createGroup(50);
    createText(getI18NString('SYS9'), 3550,2200,200, "#F00", group9);
    var group10 = createGroup(50);
    createText(getI18NString('SYS10'), 5050,2000,200, "#F00", group10);
    if(!Q.Element.prototype.initAlarmBalloon){
    	  Q.Element.prototype.initAlarmBalloon = function(){
    	      var alarmUI = new Q.LabelUI();
    	      alarmUI.position = Q.Position.CENTER_TOP;
    	      alarmUI.anchorPosition = Q.Position.LEFT_BOTTOM;
    	      alarmUI.border = 1;
    	      alarmUI.backgroundGradient = Q.Gradient.LINEAR_GRADIENT_VERTICAL;
    	      alarmUI.padding = new Q.Insets(2, 5);
    	      alarmUI.showPointer = true;
    	      alarmUI.offsetY = -10;
    	      alarmUI.offsetX = -10;
    	      alarmUI.rotatable = false;
    	      alarmUI.showOnTop = true;
    	      this._alarmBalloon = alarmUI;
    	  }
    	  Q.Element.prototype._checkAlarmBalloon = function(){
    	      if(!this.alarmLabel || !this.alarmColor){
    	          if(this._alarmBalloon){
    	              this.removeUI(this._alarmBalloon);
    	          }
    	          return;
    	      }
    	      if(!this._alarmBalloon){
    	          this.initAlarmBalloon();
    	      }
    	      this._alarmBalloon.data = this.alarmLabel;
    	      this._alarmBalloon.backgroundColor = this.alarmColor;
    	      if(this.addUI(this._alarmBalloon) === false){
    	          this.invalidate();
    	      }
    	  }
    	  Q.Element.prototype.setAlarm = function(alarmLabel, alarmColor){
    	      this.alarmColor = alarmColor;
    	      this.alarmLabel = alarmLabel;
    	  }
    	  Object.defineProperties(Q.Element.prototype, {
    	      alarmLabel: {
    	          get: function(){
    	              return this._alarmLabel;
    	          },
    	          set: function(label){
    	              if(this._alarmLabel == label){
    	                  return;
    	              }
    	              this._alarmLabel = label;
    	              this._checkAlarmBalloon();
    	          }
    	      },
    	      alarmColor: {
    	          get: function(){
    	              return this._alarmColor;
    	          },
    	          set: function(color){
    	              if(this._alarmColor == color){
    	                  return;
    	              }
    	              this._alarmColor = color;
    	              this.setStyle(Q.Styles.RENDER_COLOR, color);
    	              this._checkAlarmBalloon();
    	          }
    	      }
    	  })
    	}
    function createNode(image, x, y, name, group){
        var node = graph.createNode(name, x, y);
        if(image){
            if(Q.isString(image)){
                image = "${pageContext.request.contextPath}/static/qunee/images2/" + image;
            }
            node.image = image;
        }
        if(group){
            group.addChild(node);
        }
        return node;
    }


    function createText(name, x, y, fontSize, color, parent){
        var text = graph.createText(name, x, y);
        text.setStyle(Q.Styles.LABEL_ANCHOR_POSITION, Q.Position.CENTER_MIDDLE);
        text.setStyle(Q.Styles.LABEL_POSITION, Q.Position.CENTER_MIDDLE);
        text.setStyle(Q.Styles.LABEL_FONT_SIZE, fontSize);
        text.setStyle(Q.Styles.LABEL_COLOR, color);
        text.setStyle(Q.Styles.LABEL_BACKGROUND_COLOR, null);
        if(parent){
            parent.addChild(text);
        }
        return text;
    }

    function createGroup(padding){
        var group = graph.createGroup();
        group.groupImage = graphs.group_cloud;
        group.padding = padding || 30;
        return group;
    }

    function createEdge(a, b, color, dashed, name){
        var edge = graph.createEdge(name, a, b);
        if(dashed){
            edge.setStyle(Q.Styles.EDGE_LINE_DASH, [8, 5]);
        }
        edge.setStyle(Q.Styles.EDGE_WIDTH, 3);
        edge.setStyle(Q.Styles.EDGE_COLOR, color);
        edge.setStyle(Q.Styles.ARROW_TO, false);
        return edge;
    }
    function Check_group(name)
    {
    	switch (name) {
        case "SYS_1":
            return group1;
        case "SYS_2":
            return group2;
        case "SYS_3":
            return group3;
        case "SYS_4":
            return group4;
        case "SYS_5":
            return group5;
        case "SYS_6":
            return group6;
        case "SYS_7":
            return group7;
        case "SYS_8":
            return group8;
        case "SYS_9":
            return group9;
        case "SYS_10":
            return group10;     
    	} 
    }
    //createNode("server.png", 3880, 219, getI18NString('Storage'), group2)
    //createEdge(b, c, "#F00", true);
    function initTopology(topoNodes,topoRelations) {
        var map = {};
        for (var i = 0; i < topoNodes.length; i++) {
            var node = topoNodes[i];
            map[node.id] =createNode(node.img,node.x,node.y, getI18NString(node.name),Check_group(node.sys));
        }
        for (var i = 0; i < topoRelations.length; i++) {
            var relation = topoRelations[i];
            var nodeFrom = map[relation.from];
            var nodeTo = map[relation.to];

            if (nodeFrom && nodeTo) {
                var edge = createEdge(nodeFrom, nodeTo,relation.color);
            	
            }
        }
    }
    var VPNFlexEdgeUI = function(edge, graph){
        Q.doSuperConstructor(this, VPNFlexEdgeUI, arguments);
    }
    VPNFlexEdgeUI.prototype = {
        drawEdge: function(path, fromUI, toUI, edgeType, fromBounds, toBounds){
            var from = fromBounds.center;
            path.curveTo(from.x, from.y, internet.x, internet.y);
        }
    }

    Q.extend(VPNFlexEdgeUI, Q.EdgeUI);
    // "nodes": [{"img":"final.png","x":1105,"y":135,"name":"node_50","id":"node_50","sys":"SYS_1",},{"img":"TEST.png","x":115,"y":1305,"name":"node_5","id":"node_5","sys":"SYS_2",}],
	//"relations":[{"from":"node_50","to":"node_5", "color":"#F00"}] 
    Js_value={
    		  "nodes":[{"img":"final.png","name":"node_50","x":100,"y":100,"id":"node_50","sys":"SYS_1"},{"img":"final.png","name":"node_0","x":400,"y":100,"id":"node_0","sys":"SYS_1"},{"img":"final.png","name":"node_58","x":700,"y":100,"id":"node_58","sys":"SYS_1"},{"img":"final.png","name":"node_4","x":1000,"y":100,"id":"node_4","sys":"SYS_1"},{"img":"final.png","name":"node_83","x":100,"y":400,"id":"node_83","sys":"SYS_1"},{"img":"final.png","name":"node_33","x":400,"alarm":"端口80通信异常","y":400,"id":"node_33","sys":"SYS_1"},{"img":"final.png","name":"node_17","x":700,"y":400,"id":"node_17","sys":"SYS_1"},{"img":"final.png","name":"node_31","x":1000,"alarm":"端口8080通信异常","y":400,"id":"node_31","sys":"SYS_1"},{"img":"final.png","name":"node_15","x":100,"y":700,"id":"node_15","sys":"SYS_1"},{"img":"final.png","name":"node_73","x":400,"alarm":"url:http://node_73:80//访问失败","y":700,"id":"node_73","sys":"SYS_1"},{"img":"final.png","name":"node_93","x":700,"alarm":"端口80通信异常","y":700,"id":"node_93","sys":"SYS_1"},{"img":"final.png","name":"node_70","x":1600,"alarm":"00状态为Failed","y":100,"id":"node_70","sys":"SYS_2"},{"img":"final.png","name":"node_30","x":1900,"y":100,"id":"node_30","sys":"SYS_2"},{"img":"final.png","name":"node_45","x":2200,"y":100,"id":"node_45","sys":"SYS_2"},{"img":"final.png","name":"node_37","x":2500,"alarm":"url:http://node_37:80//访问失败","y":100,"id":"node_37","sys":"SYS_2"},{"img":"final.png","name":"node_55","x":1600,"y":400,"id":"node_55","sys":"SYS_2"},{"img":"final.png","name":"node_21","x":1900,"y":400,"id":"node_21","sys":"SYS_2"},{"img":"final.png","name":"node_18","x":2200,"y":400,"id":"node_18","sys":"SYS_2"},{"img":"final.png","name":"node_7","x":2500,"y":400,"id":"node_7","sys":"SYS_2"},{"img":"final.png","name":"node_99","x":1600,"y":700,"id":"node_99","sys":"SYS_2"},{"img":"final.png","name":"node_8","x":1900,"y":700,"id":"node_8","sys":"SYS_2"},{"img":"final.png","name":"node_91","x":2200,"y":700,"id":"node_91","sys":"SYS_2"},{"img":"final.png","name":"node_57","x":3100,"y":100,"id":"node_57","sys":"SYS_3"},{"img":"final.png","name":"node_20","x":3400,"y":100,"id":"node_20","sys":"SYS_3"},{"img":"final.png","name":"node_28","x":3700,"y":100,"id":"node_28","sys":"SYS_3"},{"img":"final.png","name":"node_3","x":4000,"y":100,"id":"node_3","sys":"SYS_3"},{"img":"final.png","name":"node_97","x":3100,"y":400,"id":"node_97","sys":"SYS_3"},{"img":"final.png","name":"node_39","x":3400,"y":400,"id":"node_39","sys":"SYS_3"},{"img":"final.png","name":"node_86","x":3700,"y":400,"id":"node_86","sys":"SYS_3"},{"img":"final.png","name":"node_94","x":4000,"y":400,"id":"node_94","sys":"SYS_3"},{"img":"final.png","name":"node_72","x":4600,"y":100,"id":"node_72","sys":"SYS_4"},{"img":"final.png","name":"node_34","x":4900,"alarm":"端口80通信异常","y":100,"id":"node_34","sys":"SYS_4"},{"img":"final.png","name":"node_81","x":5200,"alarm":"80端口的连接数大于2000","y":100,"id":"node_81","sys":"SYS_4"},{"img":"final.png","name":"node_36","x":5500,"alarm":"端口80通信异常","y":100,"id":"node_36","sys":"SYS_4"},{"img":"final.png","name":"node_62","x":4600,"y":400,"id":"node_62","sys":"SYS_4"},{"img":"final.png","name":"node_77","x":4900,"y":400,"id":"node_77","sys":"SYS_4"},{"img":"final.png","name":"node_69","x":5200,"y":400,"id":"node_69","sys":"SYS_4"},{"img":"final.png","name":"node_13","x":5500,"alarm":"url:http://node_13:80//访问失败","y":400,"id":"node_13","sys":"SYS_4"},{"img":"final.png","name":"node_9","x":4600,"y":700,"id":"node_9","sys":"SYS_4"},{"img":"final.png","name":"node_19","x":4900,"alarm":"端口80通信异常","y":700,"id":"node_19","sys":"SYS_4"},{"img":"final.png","name":"node_27","x":5200,"alarm":"url:http://node_27:8080访问失败","y":700,"id":"node_27","sys":"SYS_4"},{"img":"final.png","name":"node_5","x":5500,"y":700,"id":"node_5","sys":"SYS_4"},{"img":"final.png","name":"node_14","x":100,"alarm":"日志报错:无法获取连接","y":1000,"id":"node_14","sys":"SYS_5"},{"img":"final.png","name":"node_26","x":400,"y":1000,"id":"node_26","sys":"SYS_5"},{"img":"final.png","name":"node_65","x":700,"alarm":"停止运行","y":1000,"id":"node_65","sys":"SYS_5"},{"img":"final.png","name":"node_2","x":1000,"y":1000,"id":"node_2","sys":"SYS_5"},{"img":"final.png","name":"node_76","x":100,"y":1300,"id":"node_76","sys":"SYS_5"},{"img":"final.png","name":"node_38","x":400,"alarm":"停止运行","y":1300,"id":"node_38","sys":"SYS_5"},{"img":"final.png","name":"node_82","x":700,"y":1300,"id":"node_82","sys":"SYS_5"},{"img":"final.png","name":"node_60","x":1000,"alarm":"端口80通信异常","y":1300,"id":"node_60","sys":"SYS_5"},{"img":"final.png","name":"node_6","x":100,"alarm":"日志中有OutOfMemoryError信息","y":1600,"id":"node_6","sys":"SYS_5"},{"img":"final.png","name":"node_74","x":400,"y":1600,"id":"node_74","sys":"SYS_5"},{"img":"final.png","name":"node_85","x":700,"y":1600,"id":"node_85","sys":"SYS_5"},{"img":"final.png","name":"node_56","x":4600,"y":1000,"id":"node_56","sys":"SYS_6"},{"img":"final.png","name":"node_67","x":4900,"alarm":"端口8080通信异常","y":1000,"id":"node_67","sys":"SYS_6"},{"img":"final.png","name":"node_25","x":5200,"y":1000,"id":"node_25","sys":"SYS_6"},{"img":"final.png","name":"node_48","x":5500,"y":1000,"id":"node_48","sys":"SYS_6"},{"img":"final.png","name":"node_59","x":4600,"alarm":"ping丢包率100%,服务器宕机","y":1300,"id":"node_59","sys":"SYS_6"},{"img":"final.png","name":"node_32","x":4900,"alarm":"日志中有OutOfMemoryError信息","y":1300,"id":"node_32","sys":"SYS_6"},{"img":"final.png","name":"node_35","x":5200,"alarm":"端口8080通信异常","y":1300,"id":"node_35","sys":"SYS_6"},{"img":"final.png","name":"node_46","x":5500,"y":1300,"id":"node_46","sys":"SYS_6"},{"img":"final.png","name":"node_1","x":4600,"y":1600,"id":"node_1","sys":"SYS_6"},{"img":"final.png","name":"node_98","x":4900,"y":1600,"id":"node_98","sys":"SYS_6"},{"img":"final.png","name":"node_63","x":100,"y":1900,"id":"node_63","sys":"SYS_7"},{"img":"final.png","name":"node_53","x":400,"alarm":"网卡流量unknown","y":1900,"id":"node_53","sys":"SYS_7"},{"img":"final.png","name":"node_61","x":700,"y":1900,"id":"node_61","sys":"SYS_7"},{"img":"final.png","name":"node_89","x":1000,"y":1900,"id":"node_89","sys":"SYS_7"},{"img":"final.png","name":"node_54","x":100,"y":2200,"id":"node_54","sys":"SYS_7"},{"img":"final.png","name":"node_24","x":400,"y":2200,"id":"node_24","sys":"SYS_7"},{"img":"final.png","name":"node_23","x":700,"y":2200,"id":"node_23","sys":"SYS_7"},{"img":"final.png","name":"node_51","x":1000,"y":2200,"id":"node_51","sys":"SYS_7"},{"img":"final.png","name":"node_84","x":1600,"alarm":"url:http://node_84:8080访问失败","y":1900,"id":"node_84","sys":"SYS_8"},{"img":"final.png","name":"node_10","x":1900,"y":1900,"id":"node_10","sys":"SYS_8"},{"img":"final.png","name":"node_49","x":2200,"y":1900,"id":"node_49","sys":"SYS_8"},{"img":"final.png","name":"node_95","x":2500,"alarm":"端口8080通信异常","y":1900,"id":"node_95","sys":"SYS_8"},{"img":"final.png","name":"node_88","x":1600,"alarm":"ping丢包率100%,服务器宕机","y":2200,"id":"node_88","sys":"SYS_8"},{"img":"final.png","name":"node_43","x":1900,"alarm":"停止运行","y":2200,"id":"node_43","sys":"SYS_8"},{"img":"final.png","name":"node_41","x":2200,"alarm":"ping丢包率100%,服务器宕机","y":2200,"id":"node_41","sys":"SYS_8"},{"img":"final.png","name":"node_71","x":2500,"alarm":"端口80通信异常","y":2200,"id":"node_71","sys":"SYS_8"},{"img":"final.png","name":"node_79","x":1600,"alarm":"端口8080通信异常","y":2500,"id":"node_79","sys":"SYS_8"},{"img":"final.png","name":"node_87","x":1900,"alarm":"80端口的连接数大于2000","y":2500,"id":"node_87","sys":"SYS_8"},{"img":"final.png","name":"node_68","x":3100,"y":1900,"id":"node_68","sys":"SYS_9"},{"img":"final.png","name":"node_16","x":3400,"alarm":"停止运行","y":1900,"id":"node_16","sys":"SYS_9"},{"img":"final.png","name":"node_92","x":3700,"alarm":"日志报错:无法获取连接","y":1900,"id":"node_92","sys":"SYS_9"},{"img":"final.png","name":"node_78","x":4000,"y":1900,"id":"node_78","sys":"SYS_9"},{"img":"final.png","name":"node_47","x":3100,"alarm":"日志报错:无法获取连接","y":2200,"id":"node_47","sys":"SYS_9"},{"img":"final.png","name":"node_75","x":3400,"y":2200,"id":"node_75","sys":"SYS_9"},{"img":"final.png","name":"node_22","x":3700,"alarm":"停止运行","y":2200,"id":"node_22","sys":"SYS_9"},{"img":"final.png","name":"node_80","x":4000,"alarm":"端口80通信异常","y":2200,"id":"node_80","sys":"SYS_9"},{"img":"final.png","name":"node_66","x":3100,"y":2500,"id":"node_66","sys":"SYS_9"},{"img":"final.png","name":"node_12","x":3400,"alarm":"80端口的连接数大于2000","y":2500,"id":"node_12","sys":"SYS_9"},{"img":"final.png","name":"node_44","x":3700,"alarm":"url:http://node_44:80//访问失败","y":2500,"id":"node_44","sys":"SYS_9"},{"img":"final.png","name":"node_29","x":4600,"y":1900,"id":"node_29","sys":"SYS_10"},{"img":"final.png","name":"node_64","x":4900,"y":1900,"id":"node_64","sys":"SYS_10"},{"img":"final.png","name":"node_96","x":5200,"y":1900,"id":"node_96","sys":"SYS_10"},{"img":"final.png","name":"node_42","x":5500,"alarm":"端口80通信异常","y":1900,"id":"node_42","sys":"SYS_10"},{"img":"final.png","name":"node_90","x":4600,"alarm":"端口80通信异常","y":2200,"id":"node_90","sys":"SYS_10"},{"img":"final.png","name":"node_11","x":4900,"alarm":"url:http://node_11:80//访问失败","y":2200,"id":"node_11","sys":"SYS_10"},{"img":"final.png","name":"node_52","x":5200,"alarm":"端口80通信异常","y":2200,"id":"node_52","sys":"SYS_10"},{"img":"final.png","name":"node_40","x":5500,"y":2200,"id":"node_40","sys":"SYS_10"}]
,    		  "relations":[{"color":"#45E","from":"node_50","to":"node_4"},{"color":"#45E","from":"node_50","to":"node_83"},{"color":"#F00","from":"node_50","to":"node_33"},{"color":"#45E","from":"node_50","to":"node_17"},{"color":"#45E","from":"node_0","to":"node_4"},{"color":"#45E","from":"node_0","to":"node_83"},{"color":"#F00","from":"node_0","to":"node_33"},{"color":"#45E","from":"node_0","to":"node_17"},{"color":"#45E","from":"node_58","to":"node_4"},{"color":"#45E","from":"node_58","to":"node_83"},{"color":"#F00","from":"node_58","to":"node_33"},{"color":"#45E","from":"node_58","to":"node_17"},{"color":"#F00","from":"node_4","to":"node_31"},{"color":"#45E","from":"node_4","to":"node_15"},{"color":"#F00","from":"node_4","to":"node_73"},{"color":"#F00","from":"node_4","to":"node_93"},{"color":"#F00","from":"node_83","to":"node_31"},{"color":"#45E","from":"node_83","to":"node_15"},{"color":"#F00","from":"node_83","to":"node_73"},{"color":"#F00","from":"node_83","to":"node_93"},{"color":"#F00","from":"node_33","to":"node_31"},{"color":"#45E","from":"node_33","to":"node_15"},{"color":"#F00","from":"node_33","to":"node_73"},{"color":"#F00","from":"node_33","to":"node_93"},{"color":"#F00","from":"node_17","to":"node_31"},{"color":"#45E","from":"node_17","to":"node_15"},{"color":"#F00","from":"node_17","to":"node_73"},{"color":"#F00","from":"node_17","to":"node_93"},{"color":"#F00","from":"node_70","to":"node_37"},{"color":"#45E","from":"node_70","to":"node_55"},{"color":"#45E","from":"node_70","to":"node_21"},{"color":"#F00","from":"node_30","to":"node_37"},{"color":"#45E","from":"node_30","to":"node_55"},{"color":"#45E","from":"node_30","to":"node_21"},{"color":"#F00","from":"node_45","to":"node_37"},{"color":"#45E","from":"node_45","to":"node_55"},{"color":"#45E","from":"node_45","to":"node_21"},{"color":"#45E","from":"node_37","to":"node_18"},{"color":"#45E","from":"node_37","to":"node_7"},{"color":"#45E","from":"node_37","to":"node_99"},{"color":"#45E","from":"node_37","to":"node_8"},{"color":"#45E","from":"node_37","to":"node_91"},{"color":"#45E","from":"node_55","to":"node_18"},{"color":"#45E","from":"node_55","to":"node_7"},{"color":"#45E","from":"node_55","to":"node_99"},{"color":"#45E","from":"node_55","to":"node_8"},{"color":"#45E","from":"node_55","to":"node_91"},{"color":"#45E","from":"node_21","to":"node_18"},{"color":"#45E","from":"node_21","to":"node_7"},{"color":"#45E","from":"node_21","to":"node_99"},{"color":"#45E","from":"node_21","to":"node_8"},{"color":"#45E","from":"node_21","to":"node_91"},{"color":"#45E","from":"node_57","to":"node_28"},{"color":"#45E","from":"node_57","to":"node_3"},{"color":"#45E","from":"node_57","to":"node_97"},{"color":"#45E","from":"node_20","to":"node_28"},{"color":"#45E","from":"node_20","to":"node_3"},{"color":"#45E","from":"node_20","to":"node_97"},{"color":"#45E","from":"node_28","to":"node_39"},{"color":"#45E","from":"node_28","to":"node_86"},{"color":"#45E","from":"node_28","to":"node_94"},{"color":"#45E","from":"node_3","to":"node_39"},{"color":"#45E","from":"node_3","to":"node_86"},{"color":"#45E","from":"node_3","to":"node_94"},{"color":"#45E","from":"node_97","to":"node_39"},{"color":"#45E","from":"node_97","to":"node_86"},{"color":"#45E","from":"node_97","to":"node_94"},{"color":"#45E","from":"node_72","to":"node_62"},{"color":"#45E","from":"node_72","to":"node_77"},{"color":"#45E","from":"node_34","to":"node_62"},{"color":"#45E","from":"node_34","to":"node_77"},{"color":"#45E","from":"node_81","to":"node_62"},{"color":"#45E","from":"node_81","to":"node_77"},{"color":"#45E","from":"node_36","to":"node_62"},{"color":"#45E","from":"node_36","to":"node_77"},{"color":"#45E","from":"node_62","to":"node_69"},{"color":"#F00","from":"node_62","to":"node_13"},{"color":"#45E","from":"node_62","to":"node_9"},{"color":"#F00","from":"node_62","to":"node_19"},{"color":"#F00","from":"node_62","to":"node_27"},{"color":"#45E","from":"node_62","to":"node_5"},{"color":"#45E","from":"node_77","to":"node_69"},{"color":"#F00","from":"node_77","to":"node_13"},{"color":"#45E","from":"node_77","to":"node_9"},{"color":"#F00","from":"node_77","to":"node_19"},{"color":"#F00","from":"node_77","to":"node_27"},{"color":"#45E","from":"node_77","to":"node_5"},{"color":"#F00","from":"node_14","to":"node_65"},{"color":"#45E","from":"node_14","to":"node_2"},{"color":"#45E","from":"node_14","to":"node_76"},{"color":"#F00","from":"node_14","to":"node_38"},{"color":"#F00","from":"node_26","to":"node_65"},{"color":"#45E","from":"node_26","to":"node_2"},{"color":"#45E","from":"node_26","to":"node_76"},{"color":"#F00","from":"node_26","to":"node_38"},{"color":"#45E","from":"node_65","to":"node_82"},{"color":"#F00","from":"node_65","to":"node_60"},{"color":"#F00","from":"node_65","to":"node_6"},{"color":"#45E","from":"node_65","to":"node_74"},{"color":"#45E","from":"node_65","to":"node_85"},{"color":"#45E","from":"node_2","to":"node_82"},{"color":"#F00","from":"node_2","to":"node_60"},{"color":"#F00","from":"node_2","to":"node_6"},{"color":"#45E","from":"node_2","to":"node_74"},{"color":"#45E","from":"node_2","to":"node_85"},{"color":"#45E","from":"node_76","to":"node_82"},{"color":"#F00","from":"node_76","to":"node_60"},{"color":"#F00","from":"node_76","to":"node_6"},{"color":"#45E","from":"node_76","to":"node_74"},{"color":"#45E","from":"node_76","to":"node_85"},{"color":"#45E","from":"node_38","to":"node_82"},{"color":"#F00","from":"node_38","to":"node_60"},{"color":"#F00","from":"node_38","to":"node_6"},{"color":"#45E","from":"node_38","to":"node_74"},{"color":"#45E","from":"node_38","to":"node_85"},{"color":"#45E","from":"node_56","to":"node_25"},{"color":"#45E","from":"node_56","to":"node_48"},{"color":"#F00","from":"node_56","to":"node_59"},{"color":"#F00","from":"node_56","to":"node_32"},{"color":"#45E","from":"node_67","to":"node_25"},{"color":"#45E","from":"node_67","to":"node_48"},{"color":"#F00","from":"node_67","to":"node_59"},{"color":"#F00","from":"node_67","to":"node_32"},{"color":"#F00","from":"node_25","to":"node_35"},{"color":"#45E","from":"node_25","to":"node_46"},{"color":"#45E","from":"node_25","to":"node_1"},{"color":"#45E","from":"node_25","to":"node_98"},{"color":"#F00","from":"node_48","to":"node_35"},{"color":"#45E","from":"node_48","to":"node_46"},{"color":"#45E","from":"node_48","to":"node_1"},{"color":"#45E","from":"node_48","to":"node_98"},{"color":"#F00","from":"node_59","to":"node_35"},{"color":"#45E","from":"node_59","to":"node_46"},{"color":"#45E","from":"node_59","to":"node_1"},{"color":"#45E","from":"node_59","to":"node_98"},{"color":"#F00","from":"node_32","to":"node_35"},{"color":"#45E","from":"node_32","to":"node_46"},{"color":"#45E","from":"node_32","to":"node_1"},{"color":"#45E","from":"node_32","to":"node_98"},{"color":"#45E","from":"node_63","to":"node_61"},{"color":"#45E","from":"node_63","to":"node_89"},{"color":"#45E","from":"node_53","to":"node_61"},{"color":"#45E","from":"node_53","to":"node_89"},{"color":"#45E","from":"node_61","to":"node_54"},{"color":"#45E","from":"node_61","to":"node_24"},{"color":"#45E","from":"node_61","to":"node_23"},{"color":"#45E","from":"node_61","to":"node_51"},{"color":"#45E","from":"node_89","to":"node_54"},{"color":"#45E","from":"node_89","to":"node_24"},{"color":"#45E","from":"node_89","to":"node_23"},{"color":"#45E","from":"node_89","to":"node_51"},{"color":"#F00","from":"node_84","to":"node_88"},{"color":"#F00","from":"node_84","to":"node_43"},{"color":"#F00","from":"node_84","to":"node_41"},{"color":"#F00","from":"node_10","to":"node_88"},{"color":"#F00","from":"node_10","to":"node_43"},{"color":"#F00","from":"node_10","to":"node_41"},{"color":"#F00","from":"node_49","to":"node_88"},{"color":"#F00","from":"node_49","to":"node_43"},{"color":"#F00","from":"node_49","to":"node_41"},{"color":"#F00","from":"node_95","to":"node_88"},{"color":"#F00","from":"node_95","to":"node_43"},{"color":"#F00","from":"node_95","to":"node_41"},{"color":"#F00","from":"node_88","to":"node_71"},{"color":"#F00","from":"node_88","to":"node_79"},{"color":"#F00","from":"node_88","to":"node_87"},{"color":"#F00","from":"node_43","to":"node_71"},{"color":"#F00","from":"node_43","to":"node_79"},{"color":"#F00","from":"node_43","to":"node_87"},{"color":"#F00","from":"node_41","to":"node_71"},{"color":"#F00","from":"node_41","to":"node_79"},{"color":"#F00","from":"node_41","to":"node_87"},{"color":"#F00","from":"node_68","to":"node_47"},{"color":"#45E","from":"node_68","to":"node_75"},{"color":"#F00","from":"node_16","to":"node_47"},{"color":"#45E","from":"node_16","to":"node_75"},{"color":"#F00","from":"node_92","to":"node_47"},{"color":"#45E","from":"node_92","to":"node_75"},{"color":"#F00","from":"node_78","to":"node_47"},{"color":"#45E","from":"node_78","to":"node_75"},{"color":"#F00","from":"node_47","to":"node_22"},{"color":"#F00","from":"node_47","to":"node_80"},{"color":"#45E","from":"node_47","to":"node_66"},{"color":"#F00","from":"node_47","to":"node_12"},{"color":"#F00","from":"node_47","to":"node_44"},{"color":"#F00","from":"node_75","to":"node_22"},{"color":"#F00","from":"node_75","to":"node_80"},{"color":"#45E","from":"node_75","to":"node_66"},{"color":"#F00","from":"node_75","to":"node_12"},{"color":"#F00","from":"node_75","to":"node_44"},{"color":"#F00","from":"node_29","to":"node_42"},{"color":"#F00","from":"node_29","to":"node_90"},{"color":"#F00","from":"node_29","to":"node_11"},{"color":"#F00","from":"node_64","to":"node_42"},{"color":"#F00","from":"node_64","to":"node_90"},{"color":"#F00","from":"node_64","to":"node_11"},{"color":"#F00","from":"node_96","to":"node_42"},{"color":"#F00","from":"node_96","to":"node_90"},{"color":"#F00","from":"node_96","to":"node_11"},{"color":"#F00","from":"node_42","to":"node_52"},{"color":"#45E","from":"node_42","to":"node_40"},{"color":"#F00","from":"node_90","to":"node_52"},{"color":"#45E","from":"node_90","to":"node_40"},{"color":"#F00","from":"node_11","to":"node_52"},{"color":"#45E","from":"node_11","to":"node_40"},{"color":"#45E","from":"node_31","to":"node_63"},{"color":"#F00","from":"node_31","to":"node_53"},{"color":"#45E","from":"node_31","to":"node_68"},{"color":"#F00","from":"node_31","to":"node_16"},{"color":"#F00","from":"node_31","to":"node_92"},{"color":"#45E","from":"node_31","to":"node_78"},{"color":"#45E","from":"node_15","to":"node_63"},{"color":"#F00","from":"node_15","to":"node_53"},{"color":"#45E","from":"node_15","to":"node_68"},{"color":"#F00","from":"node_15","to":"node_16"},{"color":"#F00","from":"node_15","to":"node_92"},{"color":"#45E","from":"node_15","to":"node_78"},{"color":"#45E","from":"node_73","to":"node_63"},{"color":"#F00","from":"node_73","to":"node_53"},{"color":"#45E","from":"node_73","to":"node_68"},{"color":"#F00","from":"node_73","to":"node_16"},{"color":"#F00","from":"node_73","to":"node_92"},{"color":"#45E","from":"node_73","to":"node_78"},{"color":"#45E","from":"node_93","to":"node_63"},{"color":"#F00","from":"node_93","to":"node_53"},{"color":"#45E","from":"node_93","to":"node_68"},{"color":"#F00","from":"node_93","to":"node_16"},{"color":"#F00","from":"node_93","to":"node_92"},{"color":"#45E","from":"node_93","to":"node_78"},{"color":"#F00","from":"node_18","to":"node_84"},{"color":"#45E","from":"node_18","to":"node_10"},{"color":"#45E","from":"node_18","to":"node_49"},{"color":"#F00","from":"node_18","to":"node_95"},{"color":"#F00","from":"node_7","to":"node_84"},{"color":"#45E","from":"node_7","to":"node_10"},{"color":"#45E","from":"node_7","to":"node_49"},{"color":"#F00","from":"node_7","to":"node_95"},{"color":"#F00","from":"node_99","to":"node_84"},{"color":"#45E","from":"node_99","to":"node_10"},{"color":"#45E","from":"node_99","to":"node_49"},{"color":"#F00","from":"node_99","to":"node_95"},{"color":"#F00","from":"node_8","to":"node_84"},{"color":"#45E","from":"node_8","to":"node_10"},{"color":"#45E","from":"node_8","to":"node_49"},{"color":"#F00","from":"node_8","to":"node_95"},{"color":"#F00","from":"node_91","to":"node_84"},{"color":"#45E","from":"node_91","to":"node_10"},{"color":"#45E","from":"node_91","to":"node_49"},{"color":"#F00","from":"node_91","to":"node_95"},{"color":"#45E","from":"node_39","to":"node_56"},{"color":"#F00","from":"node_39","to":"node_67"},{"color":"#F00","from":"node_39","to":"node_84"},{"color":"#45E","from":"node_39","to":"node_10"},{"color":"#45E","from":"node_39","to":"node_49"},{"color":"#F00","from":"node_39","to":"node_95"},{"color":"#45E","from":"node_86","to":"node_56"},{"color":"#F00","from":"node_86","to":"node_67"},{"color":"#F00","from":"node_86","to":"node_84"},{"color":"#45E","from":"node_86","to":"node_10"},{"color":"#45E","from":"node_86","to":"node_49"},{"color":"#F00","from":"node_86","to":"node_95"},{"color":"#45E","from":"node_94","to":"node_56"},{"color":"#F00","from":"node_94","to":"node_67"},{"color":"#F00","from":"node_94","to":"node_84"},{"color":"#45E","from":"node_94","to":"node_10"},{"color":"#45E","from":"node_94","to":"node_49"},{"color":"#F00","from":"node_94","to":"node_95"},{"color":"#45E","from":"node_69","to":"node_50"},{"color":"#45E","from":"node_69","to":"node_0"},{"color":"#45E","from":"node_69","to":"node_58"},{"color":"#F00","from":"node_69","to":"node_14"},{"color":"#45E","from":"node_69","to":"node_26"},{"color":"#45E","from":"node_13","to":"node_50"},{"color":"#45E","from":"node_13","to":"node_0"},{"color":"#45E","from":"node_13","to":"node_58"},{"color":"#F00","from":"node_13","to":"node_14"},{"color":"#45E","from":"node_13","to":"node_26"},{"color":"#45E","from":"node_9","to":"node_50"},{"color":"#45E","from":"node_9","to":"node_0"},{"color":"#45E","from":"node_9","to":"node_58"},{"color":"#F00","from":"node_9","to":"node_14"},{"color":"#45E","from":"node_9","to":"node_26"},{"color":"#45E","from":"node_19","to":"node_50"},{"color":"#45E","from":"node_19","to":"node_0"},{"color":"#45E","from":"node_19","to":"node_58"},{"color":"#F00","from":"node_19","to":"node_14"},{"color":"#45E","from":"node_19","to":"node_26"},{"color":"#45E","from":"node_27","to":"node_50"},{"color":"#45E","from":"node_27","to":"node_0"},{"color":"#45E","from":"node_27","to":"node_58"},{"color":"#F00","from":"node_27","to":"node_14"},{"color":"#45E","from":"node_27","to":"node_26"},{"color":"#45E","from":"node_5","to":"node_50"},{"color":"#45E","from":"node_5","to":"node_0"},{"color":"#45E","from":"node_5","to":"node_58"},{"color":"#F00","from":"node_5","to":"node_14"},{"color":"#45E","from":"node_5","to":"node_26"},{"color":"#45E","from":"node_82","to":"node_56"},{"color":"#F00","from":"node_82","to":"node_67"},{"color":"#45E","from":"node_82","to":"node_63"},{"color":"#F00","from":"node_82","to":"node_53"},{"color":"#45E","from":"node_60","to":"node_56"},{"color":"#F00","from":"node_60","to":"node_67"},{"color":"#45E","from":"node_60","to":"node_63"},{"color":"#F00","from":"node_60","to":"node_53"},{"color":"#45E","from":"node_6","to":"node_56"},{"color":"#F00","from":"node_6","to":"node_67"},{"color":"#45E","from":"node_6","to":"node_63"},{"color":"#F00","from":"node_6","to":"node_53"},{"color":"#45E","from":"node_74","to":"node_56"},{"color":"#F00","from":"node_74","to":"node_67"},{"color":"#45E","from":"node_74","to":"node_63"},{"color":"#F00","from":"node_74","to":"node_53"},{"color":"#45E","from":"node_85","to":"node_56"},{"color":"#F00","from":"node_85","to":"node_67"},{"color":"#45E","from":"node_85","to":"node_63"},{"color":"#F00","from":"node_85","to":"node_53"},{"color":"#45E","from":"node_35","to":"node_72"},{"color":"#F00","from":"node_35","to":"node_34"},{"color":"#F00","from":"node_35","to":"node_81"},{"color":"#F00","from":"node_35","to":"node_36"},{"color":"#45E","from":"node_35","to":"node_29"},{"color":"#45E","from":"node_35","to":"node_64"},{"color":"#45E","from":"node_35","to":"node_96"},{"color":"#45E","from":"node_46","to":"node_72"},{"color":"#F00","from":"node_46","to":"node_34"},{"color":"#F00","from":"node_46","to":"node_81"},{"color":"#F00","from":"node_46","to":"node_36"},{"color":"#45E","from":"node_46","to":"node_29"},{"color":"#45E","from":"node_46","to":"node_64"},{"color":"#45E","from":"node_46","to":"node_96"},{"color":"#45E","from":"node_1","to":"node_72"},{"color":"#F00","from":"node_1","to":"node_34"},{"color":"#F00","from":"node_1","to":"node_81"},{"color":"#F00","from":"node_1","to":"node_36"},{"color":"#45E","from":"node_1","to":"node_29"},{"color":"#45E","from":"node_1","to":"node_64"},{"color":"#45E","from":"node_1","to":"node_96"},{"color":"#45E","from":"node_98","to":"node_72"},{"color":"#F00","from":"node_98","to":"node_34"},{"color":"#F00","from":"node_98","to":"node_81"},{"color":"#F00","from":"node_98","to":"node_36"},{"color":"#45E","from":"node_98","to":"node_29"},{"color":"#45E","from":"node_98","to":"node_64"},{"color":"#45E","from":"node_98","to":"node_96"},{"color":"#45E","from":"node_54","to":"node_57"},{"color":"#45E","from":"node_54","to":"node_20"},{"color":"#45E","from":"node_54","to":"node_29"},{"color":"#45E","from":"node_54","to":"node_64"},{"color":"#45E","from":"node_54","to":"node_96"},{"color":"#45E","from":"node_24","to":"node_57"},{"color":"#45E","from":"node_24","to":"node_20"},{"color":"#45E","from":"node_24","to":"node_29"},{"color":"#45E","from":"node_24","to":"node_64"},{"color":"#45E","from":"node_24","to":"node_96"},{"color":"#45E","from":"node_23","to":"node_57"},{"color":"#45E","from":"node_23","to":"node_20"},{"color":"#45E","from":"node_23","to":"node_29"},{"color":"#45E","from":"node_23","to":"node_64"},{"color":"#45E","from":"node_23","to":"node_96"},{"color":"#45E","from":"node_51","to":"node_57"},{"color":"#45E","from":"node_51","to":"node_20"},{"color":"#45E","from":"node_51","to":"node_29"},{"color":"#45E","from":"node_51","to":"node_64"},{"color":"#45E","from":"node_51","to":"node_96"},{"color":"#45E","from":"node_71","to":"node_72"},{"color":"#F00","from":"node_71","to":"node_34"},{"color":"#F00","from":"node_71","to":"node_81"},{"color":"#F00","from":"node_71","to":"node_36"},{"color":"#45E","from":"node_79","to":"node_72"},{"color":"#F00","from":"node_79","to":"node_34"},{"color":"#F00","from":"node_79","to":"node_81"},{"color":"#F00","from":"node_79","to":"node_36"},{"color":"#45E","from":"node_87","to":"node_72"},{"color":"#F00","from":"node_87","to":"node_34"},{"color":"#F00","from":"node_87","to":"node_81"},{"color":"#F00","from":"node_87","to":"node_36"},{"color":"#F00","from":"node_22","to":"node_70"},{"color":"#45E","from":"node_22","to":"node_30"},{"color":"#45E","from":"node_22","to":"node_45"},{"color":"#F00","from":"node_80","to":"node_70"},{"color":"#45E","from":"node_80","to":"node_30"},{"color":"#45E","from":"node_80","to":"node_45"},{"color":"#F00","from":"node_66","to":"node_70"},{"color":"#45E","from":"node_66","to":"node_30"},{"color":"#45E","from":"node_66","to":"node_45"},{"color":"#F00","from":"node_12","to":"node_70"},{"color":"#45E","from":"node_12","to":"node_30"},{"color":"#45E","from":"node_12","to":"node_45"},{"color":"#F00","from":"node_44","to":"node_70"},{"color":"#45E","from":"node_44","to":"node_30"},{"color":"#45E","from":"node_44","to":"node_45"},{"color":"#45E","from":"node_52","to":"node_72"},{"color":"#F00","from":"node_52","to":"node_34"},{"color":"#F00","from":"node_52","to":"node_81"},{"color":"#F00","from":"node_52","to":"node_36"},{"color":"#F00","from":"node_52","to":"node_70"},{"color":"#45E","from":"node_52","to":"node_30"},{"color":"#45E","from":"node_52","to":"node_45"},{"color":"#45E","from":"node_40","to":"node_72"},{"color":"#F00","from":"node_40","to":"node_34"},{"color":"#F00","from":"node_40","to":"node_81"},{"color":"#F00","from":"node_40","to":"node_36"},{"color":"#F00","from":"node_40","to":"node_70"},{"color":"#45E","from":"node_40","to":"node_30"},{"color":"#45E","from":"node_40","to":"node_45"}]
    }
    initTopology(Js_value.nodes, Js_value.relations);


	var i=0;
    var timer = setTimeout(function A(){
    	
    	var m=[]
    	$.ajax({
    		 type : "post",
    	     async : false,
    	     url : "${pageContext.request.contextPath}/Servlet_Gao",
    	     type:"POST",
    	     data:
    	     	{
    	    	 "method":"Time_qunee_fold",
    	     	"Foldname":"E:\\pycharm\\WorkPlace\\FINAL_TUO\\test"
    	     	},
    	     dataType:"json",
    		 success: function (data) {
    			 m.push(data);
    		  }
    		 });
    		var JS_NODE=m[0];
      graph.forEach(function(element){
    	  if (!(element instanceof Q.Node)) {
              return;
          }
    	  if ((element instanceof Q.Group)) {
              return;
          }
    	  if ((element instanceof Q.Text)) {
              return;
          }
	//var JS_NODE=[{"name":"node_87","alarm":"'日志中有OutOfMemoryError信息'    0.9959374157813164","id":"node_87","sys":"SYS_8"},{"name":"node_44","alarm":"'Nginx 80端口的连接数大于2000'    0.9975930295121785","id":"node_44","sys":"SYS_9"},{"name":"node_16","alarm":"'日志报错:无法获取连接'    0.974179601975923","id":"node_16","sys":"SYS_9"},{"name":"node_47","alarm":"'日志报错:无法获取连接'    0.9588165879787502","id":"node_47","sys":"SYS_9"},{"name":"node_50","alarm":"'硬盘Slot 00状态为Failed'    0.9922034884516036","id":"node_50","sys":"SYS_1"},{"name":"node_20","alarm":"'Nginx 80端口的连接数大于2000'    0.9958657238822234","id":"node_20","sys":"SYS_3"},{"name":"node_69","alarm":"'日志报错:无法获取连接'    0.8452068844884002","id":"node_69","sys":"SYS_4"},{"name":"node_54","alarm":"'网卡流量unknown'    0.9966528223567224","id":"node_54","sys":"SYS_7"},{"name":"node_41","alarm":"'端口8080通信异常'    0.9985500761191187","id":"node_41","sys":"SYS_8"},{"name":"node_40","alarm":"'端口8080通信异常'    0.9985500761191187","id":"node_40","sys":"SYS_10"},{"name":"node_71","alarm":"'日志报错:无法获取连接'    0.892037192065063","id":"node_71","sys":"SYS_8"},{"name":"node_87","alarm":"'Nginx 80端口的连接数大于2000'    0.9960469444120053","id":"node_87","sys":"SYS_8"},{"name":"node_49","alarm":"'日志报错:无法获取连接'    0.9282934664812674","id":"node_49","sys":"SYS_8"}]

    	for(var j=0;j<JS_NODE.length;j++)
    		{
    		var JS_NODE_value=JS_NODE[j];
    		var JS_NODE_value_name=JS_NODE_value["alarm"];
    		var JS_NODE_name=JS_NODE_value["name"];
    		//alert(element.name)
    		//alert(JS_NODE_name)
    		if(element.name==JS_NODE_name)
  			{
  			JS_NODE_value_name=JS_NODE_value["name"]+"\t:"+JS_NODE_value["alarm"];
  			element.parent.alarmColor = "rgba(255,246,143,1)";
             element.alarmLabel = JS_NODE_value_name;
             element.alarmColor = "rgba(255,0,0,0.93)";
             return;
  			}
    		}
    		
      	   element.alarmLabel = null;
      	   element.alarmColor = "rgba(0,255,255,0.93)";
      	   i=i+1;
      	   
      		
      	
                 
      })
      timer = setTimeout(A, 2000);
    }, 100000);

    function destroy(){
      clearTimeout(timer);
    }
</script>
</body>
</html>
