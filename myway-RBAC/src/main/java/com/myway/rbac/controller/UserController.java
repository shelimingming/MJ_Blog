package com.myway.rbac.controller;

import com.myway.rbac.common.utils.PageUtils;
import com.myway.rbac.common.utils.Query;
import com.myway.rbac.domain.UserDO;
import com.myway.rbac.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.List;
import java.util.Map;

@RequestMapping("/user")
@RestController
public class UserController {

    @Autowired
    UserService userService;

    @RequestMapping("/get")
    public UserDO get(Integer id) {
        UserDO user = userService.get(id);
        return user;
    }

    @RequestMapping("/login")
    public UserDO get(String username,String password) {
        UserDO user = userService.login(username,password);
        return user;
    }

    @PostMapping("/register")
    public int register(@RequestBody UserDO userDo) {
        userDo.setCreatetime(new Date());
        userDo.setStatus("0");
        int res = userService.register(userDo);
        return res;
    }

    @GetMapping("/list")
    @ResponseBody
    PageUtils list(@RequestParam Map<String, Object> params) {
        // 查询列表数据
        Query query = new Query(params);
        List<UserDO> sysUserList = userService.list(query);
        int total = userService.count(query);
        PageUtils pageUtil = new PageUtils(sysUserList, total);
        return pageUtil;
    }
}
