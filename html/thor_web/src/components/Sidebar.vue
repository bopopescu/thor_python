<template>
    <div class="sidebar">
        <el-col :span="4">
            <h3 class="nav_bar_title">目录</h3>
            <el-menu
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                active-text-color="#409EFF">
                <template v-for="(item, index) in nav_bar">
                    <!-- 有子列表 -->
                    <template v-if="item.subs">
                        <el-submenu :index="String(index)" :key="index">
                            <template slot="title">
                                <span>{{ item.title }}</span>
                            </template>
                            <el-menu-item-group>
                                <template v-for="(i, k) in item.subs">
                                    <el-menu-item :index="String(i.index)" :key="k">{{ i.title }}</el-menu-item>
                                </template>
                            </el-menu-item-group>
                        </el-submenu>
                    </template>

                    <!-- 没有子列表 -->
                    <template v-else>
                        <el-menu-item :index="String(index)" :key="index">
                            <span>{{ item.title }}</span>
                        </el-menu-item>
                    </template>
                </template>
            </el-menu>
        </el-col>
    </div>
</template>

<script>
	export default {
		name: "Sidebar",
        props: ['nav_bar'],
		methods: {
			handleOpen(key, keyPath) {
				console.log(key, keyPath);
			},
			handleClose(key, keyPath) {
				console.log(key, keyPath);
			}
		}
	}
</script>
