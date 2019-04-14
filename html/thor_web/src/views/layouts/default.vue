<template>
    <div class="default initial">
        <v-head/>

        <div class="x-content">
            <transition name="fade" mode="out-in">
                <router-view/>
            </transition>
        </div>

        <v-footer/>
    </div>
</template>

<script>
	export default {
		name: "default",
		data: () => ({

		})
	}
</script>
