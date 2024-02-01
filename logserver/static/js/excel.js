var vm = new Vue(
{
    el: "#container",
    data: {
        headers: [

        ],

        originTableData:[],

        tableData: [

        ],

        searchForm:{
            keyword: '',
            bu: '',
        }
    },
    created(){
        console.log("created...")
    },
    methods: {
        onSearch(){
            console.log("click search",this.searchForm)
            this.tableData = this.originTableData.filter((row)=>{

                let res = false;
                for(let k in row){
                    // console.log(k, row[k]);
                    if(row[k].indexOf(this.searchForm.keyword) != -1){
                        res = true;
                        break;
                    }
                }
//                if(row['Joined Date'] === searchForm.joinedDate){
//                    return true;
//                }
                return res;
            })
        },


        async onFileChange(e){
            const file = event.target.files[0];
            console.log("vue file:",file);
            let data = await this.readFile(file);
            this.parseExcelData(data);
        },

        readFile(file){
            return new Promise((resolve,reject) =>{
                let reader = new FileReader();
                reader.onload = function (e) {
                    resolve(e.target.result);
                };
                reader.readAsArrayBuffer(file);
            })
        },

        async parseExcelData(data){
            const workbook = XLSX.read(data); // 从原始数据获取工作簿
            // 后端使用可以使用 readFile() 方法直接读取文件

            var first_sheet_name = workbook.SheetNames[0]; // 获得第一个工作表名称

            let worksheet = workbook.Sheets[first_sheet_name]; // 获取工作表

            console.log(worksheet['B2']); // 读取并打印A1端元格数据
            console.log(worksheet['B3']);
            console.log(worksheet['C3']);
            console.log(worksheet['D3'].v);
            if(worksheet['H2'] == undefined)
                console.log("worksheet['H2']== undefined");

            const merges = worksheet['!merges']
            console.log(merges); // 打印所有合并单元格信息数组
            console.log("'!cols'="+worksheet['!cols']);
            var ak4 = worksheet['!ref'].split(':')[1]
            console.log(worksheet['!ref']); // 打印输出当前工作表使用的范围
            console.log(ak4);

            //单元格转化方法（由A1转化成{c:C, r:R}，c为行，r为列）encode_cell / decode_cell
            const cell = XLSX.utils.decode_cell(ak4);
            console.log(cell)
            console.log(cell.c)
            console.log(cell.r)

            //let jsaddr = XLSX.utils.decode_cell("B2"); // 得到{r:1, c:0}

            //let rawaddr = XLSX.utils.encode_cell({r:1, c:0}); // 得到A2

            let jsaddrr = XLSX.utils.decode_range(worksheet['!ref']); // 得到{ s: { c: 0, r: 0 }, e: { c: 3, r: 2 } }
            //let rawaddrr = XLSX.utils.encode_range({ s: { c: 0, r: 0 }, e: { c: 3, r: 2 } }); // 得到A1:D3

            console.log("range="+jsaddrr)
            $("#id_output").html(worksheet['B2'].v);

            //encode_range / decode_range（如A3:B7 互相转化 {s:{c:0, r:2}, e:{c:1, r:6}}）
            let range = XLSX.utils.decode_range(worksheet['!ref'])
            console.log("(s--e)="+range)

            this.loadExcelHeader(worksheet, range);
            this.loadExcelContent(worksheet, range);
        },

        loadExcelHeader(worksheet, range){
            let value;
            for(let C = range.s.c; C <= range.e.c; ++C) {
                var cell_address = {c:C, r:0};
                var cell_ref = XLSX.utils.encode_cell(cell_address);

                if(typeof(worksheet[cell_ref]) == "undefined" ){//把取到的数据放入表格
                    value = '';
                }else{
                    value = worksheet[cell_ref].w
                }
                this.headers.push(value);
            }

            console.log(this.header)
        },

        loadExcelContent(worksheet, range){
            for(let R = range.s.r+1; R <= range.e.r; ++R) {
                let row = {};
                for(let C = range.s.c; C <= range.e.c; ++C) {
                    var cell_address = {c:C, r:R};
                    let field = this.headers[C];
                    var cell_ref = XLSX.utils.encode_cell(cell_address);

                    if(worksheet[cell_ref]){
                        value = worksheet[cell_ref].w
                    }else{
                        value = '';
                    }


                    row[field] = value;
                }
                // console.log(row);

                this.originTableData.push(row);
                this.tableData = [...this.originTableData];
                this.$forceUpdate();
            }
            console.log(this.tableData)
        }
    }
});