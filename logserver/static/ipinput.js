


(function($)  
{  
    $.fn.ipinput = function(options)  
    {  
        // 默认属性  
        var defaults =  
        {  
            // 长度最低支持110像素  
            width : 110,  
            // 高度默认20像素  
            height : 20,  
            // 在键盘按下时用来存储未输入前的值  
            currValue : '',  
            // 原有值，就是从数据库中读取到的值  
            value : ''  
        }  
          
        // 传递的参数  
        var options = $.extend(defaults, options);  
          
        // 输入框对象及父级对象  
        var $this = $(this);  
        var $parent = $this.parent();  
          
        // 隐藏输入框（该输入框用于存储实际值）  
        $this.attr({style : 'display:none'});  
          
        // 输入控件代码  
        var html = '';  
        html += '<div class="ipinput_div">';  
        html += '<input type="text" id="ipOne" class="ipinput_input"/>';  
        html += '<span class="ipinput_separator">.</span>';  
        html += '<input type="text" id="ipTwo" class="ipinput_input"/>';  
        html += '<span class="ipinput_separator">.</span>';  
        html += '<input type="text" id="ipThree" class="ipinput_input"/>';  
        html += '<span class="ipinput_separator">.</span>';  
        html += '<input type="text" id="ipFour" class="ipinput_input"/>';  
        html += '</div>';  
          
        // 添加输入控件代码  
        $parent.append(html);  
          
        // 把原有的值赋到输入框中  
        if(!isEmpty(options.value))  
        {  
            var valArr = options.value.split(".");  
            if(4 == valArr.length)  
            {  
                $('#ipOne').val(valArr[0]);  
                $('#ipTwo').val(valArr[1]);  
                $('#ipThree').val(valArr[2]);  
                $('#ipFour').val(valArr[3]);  
            }  
        }  
          
        // 设置宽度和高度  
        $('.ipinput_div').width(options.width);  
        $('.ipinput_div').height(options.height);  
     //   alert($('input', $('.ipinput_div'))); //--fanzz 
        // 输入框绑定键盘按下事件  
        $('.ipinput_input').keydown(function(event)  
        {  
            keydown(event);  
        });  
          
        // 输入框绑定键盘按下弹起事件  
        $('.ipinput_input').keyup(function(event)  
        {  
            keyup(event);  
        });  
          
        // 输入框失去焦点事件  
        $('.ipinput_input').blur(function()  
        {  
            setData($this);  
        });  
    };  
      
    // 判断参数是否为空  
    var isEmpty = function(obj)  
    {  
        if(null == obj)  
        {  
            return true;  
        }  
        else if(undefined == obj)  
        {  
            return true;  
        }  
        else if("" == obj)  
        {  
            return true;  
        }  
        else  
        {  
            return false;  
        }  
    };  
      
    // 赋值给隐藏框  
    var setData = function(inputObj)  
    {  
        // 四个框的值  
        var one = $('#ipOne').val();  
        var two = $('#ipTwo').val();  
        var three = $('#ipThree').val();  
        var four = $('#ipFour').val();  
          
        // 如果四个框都有值则赋值给隐藏框  
        if(!isEmpty(one) && !isEmpty(two) && !isEmpty(three) && !isEmpty(four))  
        {  
            var ip = one + "." + two + "." + three + "." + four;  
            inputObj.val(ip);  
        }  
    }  
      
    // 键盘按下事件  
    var keydown = function(event)  
    {  
        // 当前输入的键盘值  
        var code = event.keyCode;  
          
        // 除了数字键、删除键、小数点之外全部不允许输入  
        if((code < 48 && 8 != code && 37 != code && 39 != code)   
            || (code > 57 && code < 96)   
            || (code > 105 && 110 != code && 190 != code))  
        {  
            return false;  
        }  
          
        // 先存储输入前的值，用于键盘弹起时判断值是否正确  
        options.currValue = $(this).val();  
          
        // 110、190代表键盘上的两个点  
        if(110 == code || 190 == code)  
        {  
            // 当前输入框的ID  
            var id = $(this).attr("id");  
              
            // 当前输入框的值  
            var value = $(this).val();  
              
            // 如果是第一个框则第二个框获的焦点  
            if("ipOne" == id && !isEmpty(value))  
            {  
                $('#ipTwo').focus();  
                return false;  
            }  
            // 如果是第二个框则第三个框获的焦点  
            else if("ipTwo" == id && !isEmpty(value))  
            {  
                $('#ipThree').focus();  
                return false;  
            }  
            // 如果是第三个框则第四个框获的焦点  
            else if("ipThree" == id && !isEmpty(value))  
            {  
                $('#ipFour').focus();  
                return false;  
            }  
            // 如果是第四个框则直接返回  
            else if("ipFour" == id)  
            {  
                return false;  
            }  
            else if(isEmpty(value))  
            {  
                return false;  
            }  
        }  
    }  
      
    // 键盘弹起事件  
    var keyup = function(event)  
    {  
        // 当前值  
        var value = $(this).val();  
        if(!isEmpty(value))  
        {  
            value = parseInt(value);  
              
            if(value > 255)  
            {  
                $(this).val(options.currValue)  
            }  
            else if(value > 99)  
            {  
                // 当前输入框的ID  
                var id = $(this).attr("id");  
                  
                // 如果是第一个框则第二个框获的焦点  
                if("ipOne" == id && !isEmpty(value))  
                {  
                    $('#ipTwo').focus();  
                }  
                // 如果是第二个框则第三个框获的焦点  
                else if("ipTwo" == id && !isEmpty(value))  
                {  
                    $('#ipThree').focus();  
                }  
                // 如果是第三个框则第四个框获的焦点  
                else if("ipThree" == id && !isEmpty(value))  
                {  
                    $('#ipFour').focus();  
                }  
            }  
        }  
    }  
})(jQuery);  
/*
//methods
function checkIpVal(item, index){ 
    let self = this;
    //确保每个值都处于0-255
    let val = item.value;
    //当输入的是空格时，值赋为空
    val = val.trim();
    val = parseInt(val, 10);
    if(isNaN(val)) {
        val = ''
    } else {
        val = val < 0 ? 0 : val;
        val = val > 255 ? 255 : val;
    }
    item.value = val;
}
function turnIpPOS(index, event) {
    let self = this;
    let e = event || window.event;
    //左箭头向左跳转，左一不做任何措施
    if(e.keyCode == 37) {
        if(index == 0) {} else {
            self.$refs.ipInput[index - 1].focus();
        }
    }
    //删除键把当前数据删除完毕后会跳转到前一个input，左一不做任何处理
    if(e.keyCode == 8) {
        let val = item.value;
        if(index == 0) {} else {
            self.$refs.ipInput[index - 1].focus();
        }
    }
    //右箭头、回车键、空格键、冒号均向右跳转，右一不做任何措施
    if(e.keyCode == 39 || e.keyCode == 13 || e.keyCode == 32 || e.keyCode == 190) {
        if(index == 3) {} else {
            self.$refs.ipInput[index + 1].focus();
        }
    }
}
function setDefaultVal(item) {
    //当input失去焦点，而ip没有赋值时，会自动赋值为0
    let self = this;
    let val = item.value;
    if(val == '') {
        item.value = '0';
    }
}

//data
ipAdress: [{
       value: ''
   }, {
       value: ''
   }, {
       value: ''
   }, {
       value: ''
   }]

*/
