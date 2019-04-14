<template>
    <div class="home">
        <!--<div class="home_inner">-->
            <!--&lt;!&ndash; left 显示更新文章标题 &ndash;&gt;-->
            <!--<div class="home_left el-col el-col-16">111</div>-->
            <!--&lt;!&ndash; right 显示常用网站 &ndash;&gt;-->
            <!--<div class="home_right el-col-3">111</div>-->
        <!--</div>-->

        <el-row :gutter="20">
            <!-- left 显示更新文章标题 -->
            <el-col :span="18">
                <div class="grid-content bg-purple-light">
                    <!-- 表单组件 -->
                    <el-table :data="articles"
                              border
                              @row-click="r_router"
                              style="width: 100%; cursor: pointer;">
                        <el-table-column prop="id" label="编号" width="200"></el-table-column>
                        <el-table-column prop="title" label="标题" min-width="500"></el-table-column>
                        <el-table-column prop="time" label="时间" width="300"></el-table-column>
                    </el-table>
                    <!-- 分页组件 -->
                    <el-pagination
                            @current-change="handleCurrentChange"
                            background
                            layout="total, prev, pager, next"
                            :total="page_num">
                    </el-pagination>
                </div>
            </el-col>

            <!-- right 显示常用网站 -->
            <el-col :span="6">
                <div class="grid-content bg-purple-light">2</div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: 'home',
        components: {

        },
        data: () => ({
            articles: [
                { id: 1, title: "vue.config.js文件配置与初步了解", time: "2019-4-13 22:40:15" },
                { id: 2, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 3, title: "使用ElementUi的layout进行布局", time: "2019-4-13 22:40:55" },
                { id: 4, title: "使用ElementUi的sidebar", time: "2019-4-13 22:40:55" },
                { id: 5, title: "初步了解yarn build进行打包", time: "2019-4-13 22:40:55" },
                { id: 6, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 7, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 8, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 9, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 10, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 11, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 12, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 13, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 14, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 15, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 16, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 17, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 18, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 19, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 20, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 21, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 22, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 23, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 24, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 25, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 26, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 27, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 28, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 29, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 30, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 31, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 32, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 33, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 34, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 35, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 36, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 37, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 38, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 39, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 40, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 41, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 42, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 43, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 44, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 45, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 46, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 47, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 48, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 49, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
                { id: 50, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 51, title: "vue.config.js文件配置与初步了解", time: "2019-4-13 22:40:15" },
				{ id: 52, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 53, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 54, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 55, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 56, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 57, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 58, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 59, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 60, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 61, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 62, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 63, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 64, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 65, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 66, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 67, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 68, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 69, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 70, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 71, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 72, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 73, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 74, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 75, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 76, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 77, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 78, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 79, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 80, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 81, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 82, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 83, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 84, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 85, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 86, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 87, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 88, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 89, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 90, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 91, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 92, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 93, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 94, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 95, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 96, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 97, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 98, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 99, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" },
				{ id: 100, title: "初步了解ElementUi使用", time: "2019-4-13 22:40:55" }
            ],
			currentPage: 5,
			cur_page: 1
        }),
        methods: {
			r_router (row) {
        		console.log(row.id)
            },
			handleSizeChange(val) {
				console.log(`每页 ${val} 条`);
			},
			handleCurrentChange(val) {
				this.cur_page = val;
			}
        },
        computed: {
        	page_num () {
        		return this.articles.length
            }
        }
    }
</script>

<style scoped>
    .el-col {
        border-radius: 5px;
    }
    .bg-purple-light {

    }
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
</style>
