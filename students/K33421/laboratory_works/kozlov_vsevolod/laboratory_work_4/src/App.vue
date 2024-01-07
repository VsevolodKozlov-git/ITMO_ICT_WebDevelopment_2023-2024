<template>
  <b-navbar toggleable="lg" type="light" variant="light">
    <b-navbar-brand href="#">LibraryApp</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item-dropdown text="Reader" right>
          <b-dropdown-item to="/reader/rare_books">With rare Books</b-dropdown-item>
          <b-dropdown-item to="/reader/outdated">With outdated</b-dropdown-item>
          <b-dropdown-item to="/reader/book_month_ago">Book a Month Ago</b-dropdown-item>
          <b-dropdown-item to="/reader/create">Create Reader</b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item to="/book_instance/list">Book Instances</b-nav-item>
        <b-nav-item to="/statistics">Statistics</b-nav-item>
        <b-nav-item-dropdown text="User" right>
          <b-dropdown-item to="/user/login">User Login</b-dropdown-item>
          <b-dropdown-item to="/user/update">User Update</b-dropdown-item>
          <b-dropdown-item to="/user/registration">User Registration</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
  <router-view></router-view>
</template>

<script setup>
import { BNavbar, BNavbarBrand, BNavbarNav, BNavbarToggle, BCollapse, BNavItemDropdown, BDropdownItem } from 'bootstrap-vue-3'

</script>

  <style scoped>
  body {
    margin: 0;
    padding: 0;
  }

  .navbar {
    margin-bottom: 0;
  }
</style>

