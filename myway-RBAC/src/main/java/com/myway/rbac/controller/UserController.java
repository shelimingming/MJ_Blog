package com.myway.rbac.controller;

import com.myway.rbac.common.utils.PageUtils;
import com.myway.rbac.common.utils.Query;
import com.myway.rbac.domain.UserDO;
import com.myway.rbac.service.UserService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiImplicitParam;
import io.swagger.annotations.ApiImplicitParams;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.Date;
import java.util.List;
import java.util.Map;

@RequestMapping("/user")
@RestController
@Api(tags = "用户管理")
public class UserController {

    @Autowired
    UserService userService;

    //使用swagger展示rest api
    //http://localhost:8003/swagger-ui.html
    @ApiOperation(value = "根据用户id查询用户", notes = "根据用户id查询用户")
    //@ApiImplicitParam(name = "id", value = "用户id", required = true, dataType = "Interger")
    @RequestMapping(value = "/{id}", method = RequestMethod.GET)
    public UserDO get(@PathVariable Integer id) {
        UserDO user = userService.get(id);
        return user;
    }

    @ApiOperation(value = "创建用户", notes = "创建用户")
    @PostMapping("/")
    public int post(@RequestBody UserDO userDo) {
        userDo.setCreatetime(new Date());
        userDo.setStatus("0");
        int res = userService.register(userDo);
        return res;
    }

    @ApiOperation(value = "用户登录", notes = "用户登录（支持手机号、邮箱登录）")
    @ApiImplicitParams({
            @ApiImplicitParam(name = "username", value = "用户名、手机号、邮箱", required = true, dataType = "String", paramType = "query"),
            @ApiImplicitParam(name = "password", value = "密码", required = true, dataType = "String", paramType = "query")
    })
    @GetMapping("/login")
    public UserDO get(String username, String password) {
        UserDO user = userService.login(username, password);
        return user;
    }

    @ApiOperation(value = "用户注册", notes = "用户注册，和创建用户创建用户功能相同，请使用创建用户接口")
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
