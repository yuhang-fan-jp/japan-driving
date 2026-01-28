<template>
  <div class="card" @click="go">
    <div class="profile">
      <div class="avatar"></div>
      <div>
        <div class="card-title">个人信息</div>
        <div class="card-desc">查看学习数据</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
const router = useRouter();

const go = () => {
  router.push("/me");
};
</script>

<style scoped>
@import "./card.css";

.profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: #ddd;
}
</style>
