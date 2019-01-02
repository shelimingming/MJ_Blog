package com.myway.rbac.service.impl;

import com.myway.rbac.dao.UserDOMapper;
import com.myway.rbac.domain.AuthDO;
import com.myway.rbac.domain.RoleDO;
import com.myway.rbac.domain.UserDO;
import com.myway.rbac.domain.UserDOExample;
import com.myway.rbac.service.AuthService;
import com.myway.rbac.service.RoleService;
import com.myway.rbac.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;
import org.springframework.util.StringUtils;

import java.util.List;
import java.util.Map;
import java.util.UUID;

@Service
public class UserServiceImpl implements UserService {

    @Autowired
    UserDOMapper userDOMapper;

    @Autowired
    AuthService authService;

    @Autowired
    RoleService roleService;

    @Override
    public UserDO get(Integer id) {
        UserDOExample example = new UserDOExample();
        example.createCriteria().andIdEqualTo(id);
        List<UserDO> userDOList = userDOMapper.selectByExample(example);

        if (CollectionUtils.isEmpty(userDOList)) {
            return null;
        } else {
            UserDO userDO = userDOList.get(0);

            List<RoleDO> roleDOList = roleService.getByUserId(userDO.getId());
            userDO.setRoleList(roleDOList);


            List<AuthDO> authDOList = authService.getByUserId(userDO.getId());
            userDO.setAuthDOList(authDOList);

            return userDO;
        }
    }

    @Override
    public UserDO login(String acct, String password) {
        if (StringUtils.isEmpty(acct) || StringUtils.isEmpty(password)) {
            return null;
        }

        //需要支持用户名、手机号、邮箱登录
        UserDOExample example = new UserDOExample();
        UserDOExample.Criteria criteria1 = example.createCriteria().andAcctEqualTo(acct);
        UserDOExample.Criteria criteria2 = example.createCriteria().andMobileEqualTo(acct);
        UserDOExample.Criteria criteria3 = example.createCriteria().andEmailEqualTo(acct);

        example.or(criteria1);
        example.or(criteria2);
        example.or(criteria3);

        List<UserDO> userDOList = userDOMapper.selectByExample(example);

        if (!CollectionUtils.isEmpty(userDOList)) {
            UserDO user = userDOList.get(0);
            if (password.equals(user.getPassword())) {
                return user;
            } else {
                return null;
            }
        } else {
            return null;
        }
    }

    @Override
    public int register(UserDO userDO) {

        int res = userDOMapper.insert(userDO);
        return res;
    }

    @Override
    public List<UserDO> list(Map<String, Object> map) {
        return null;
    }

    @Override
    public int count(Map<String, Object> map) {
        return 0;
    }

}
