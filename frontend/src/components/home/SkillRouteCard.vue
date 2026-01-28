<template>
  <div class="card" @click="go">
    <div class="card-title">技能路线</div>
    <div class="card-desc">考试路线与注意点</div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const go = () => {
  router.push("/route");
};
</script>

<style scoped>
@import "./card.css";
</style>
