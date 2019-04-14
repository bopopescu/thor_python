import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Home from '~/views/home/Home'
import Diary from '~/views/diary/Diary'

/*
	注册路由
 */
const routes = [
	{
		path: '/',
		component: Home,
		alias: '/home'
	},
	{
		path: '/diary',
		component: Diary
	}
];

/*
	创建router对象函数
 */

function createRouter () {
	const router = new Router({
		mode: 'history',
		routes
	});
	router.beforeEach(beforeEach);
	return router
}

const router = createRouter();

export default router

/*
	router守卫函数
	用于判断路由
 */

async function beforeEach(to, from, next) {

	const components = await resolveComponents(router.getMatchedComponents(to));

	if (components.length === 0) {
		return next();
	}

	let to_path = to.path;

	let layout = to_path === '/login' || to_path === '/register' ? 'auth' : 'default';

	router.app.setLayout(layout)

	next();
}

/*
	resolve component 函数用于解析组件返回结果
 */

function resolveComponents (components) {
	return Promise.all(components.map(component => {
		return typeof component === 'function' ? component() : component;
	}))
}
