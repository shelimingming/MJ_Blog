package com.myway.blog.service.impl;

import com.myway.blog.dao.BlogDOMapper;
import com.myway.blog.domain.BlogDO;
import com.myway.blog.domain.BlogDOExample;
import com.myway.blog.service.BlogService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.util.List;
import java.util.Map;

@Service
public class BlogServiceImpl implements BlogService {

    @Autowired
    BlogDOMapper blogDOMapper;

    @Override
    public BlogDO get(Integer id) {
        BlogDOExample example = new BlogDOExample();
        example.createCriteria().andIdEqualTo(id);
        List<BlogDO> blogDOList = blogDOMapper.selectByExample(example);

        if(CollectionUtils.isEmpty(blogDOList)) {
            return null;
        }else{
            return blogDOList.get(0);
        }
    }

    @Override
    public List<BlogDO> list(Map<String, Object> map) {
        BlogDOExample example = new BlogDOExample();
        List<BlogDO> blogDOList = blogDOMapper.selectByExample(example);
        return blogDOList;
    }

    @Override
    public int count(Map<String, Object> map) {
        return 0;
    }

}
