<template>
    <div id="app">
        <transition name="page" mode="out-in">
            <component v-if="layout" :is="layout"/>
        </transition>
    </div>
</template>

<script>
    import Auth from './views/layouts/auth'
    import Default from './views/layouts/default'
    import Basic from './views/layouts/basic'
    export default {
        name: 'App',
        data: () => ({
            layout: null,
            defaultLayout: 'default'
        }),
        components: {
        	Auth, Default, Basic
        },
		methods: {
			setLayout (layout) {
        		this.layout = layout
            }
        }
    }
</script>
