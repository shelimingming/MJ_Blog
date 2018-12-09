package com.myway.blog.service;

import com.myway.blog.domain.BlogDO;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public interface BlogService {
    BlogDO get(Integer id);

    List<BlogDO> list(Map<String, Object> map);

    int count(Map<String, Object> map);
}
