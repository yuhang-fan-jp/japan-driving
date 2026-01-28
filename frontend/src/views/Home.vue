<template>
  <div class="container">
    <AppCard class="full" @click="go('/history')">
      <h3>历史记录</h3>
      <p>得分 & 用时趋势</p>
    </AppCard>

    <div class="grid">
      <AppCard @click="go('/practice')">知识练习</AppCard>
      <AppCard @click="go('/skills')">技能路线</AppCard>
      <AppCard @click="go('/wrong')">错题复习</AppCard>
      <AppCard @click="go('/profile')">个人信息</AppCard>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import AppCard from "../components/AppCard.vue";

const router = useRouter();
const go = (path: string) => router.push(path);
</script>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 24px;
}

.full {
  margin-bottom: 24px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
</style>