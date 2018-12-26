package com.myway.blog.controller;

import com.myway.blog.domain.BlogDO;
import com.myway.blog.service.BlogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RequestMapping("/blog")
@RestController
public class BlogController {

    @Autowired
    BlogService blogService;

    @RequestMapping("/get")
    public BlogDO get(Integer id) {
        BlogDO blog = blogService.get(id);
        return blog;
    }

    //测试使用，正式勿用用
    @RequestMapping("/getAll")
    public List<BlogDO> get() {
        List<BlogDO> blogList = blogService.list(null);
        return blogList;
    }

//    @GetMapping("/list")
//    @ResponseBody
//    PageUtils list(@RequestParam Map<String, Object> params) {
//        // 查询列表数据
//        Query query = new Query(params);
//        List<UserDO> sysUserList = userService.list(query);
//        int total = userService.count(query);
//        PageUtils pageUtil = new PageUtils(sysUserList, total);
//        return pageUtil;
//    }
}
