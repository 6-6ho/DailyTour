package com.daily.tour.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@Table(name="REG_ATTRS_TB")
@Entity
@NoArgsConstructor
public class RegAttrsEntity {
    @Id
    @Column(name="attr_code")
    private String attrCode;
    @Column(name="reg_code")
    private String regCode;
    @Column(name="attrName")
    private String attrName;
}
