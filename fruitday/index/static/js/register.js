$(function(){
  //1. 为表单绑定提交事件
  $('#formReg').submit(function(){
    //判断upwd 和 cpwd 的值是否相等
    if($("#upwd").val() != $("#cpwd").val()){
      alert("两次密码输入不一致");
      return false;
    }
    return true;
  });
});