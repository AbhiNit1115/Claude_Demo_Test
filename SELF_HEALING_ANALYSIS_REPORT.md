# Self-Healing Regression Test Analysis Report

**Generated:** 2026-04-17 09:00 UTC  
**PR:** #5 - Demo: Self-healing regression test suite  
**Branch:** `test/self-healing-demo`  
**Test File:** `Typi_Code_Tests/Test_Scripts/test_self_healing_demo.py`

---

## Executive Summary

A comprehensive self-healing regression test suite was created with 7 intentionally failing test cases to demonstrate automated error detection, analysis, and correction mechanisms. All 7 tests failed during initial execution with clearly identifiable root causes.

**Key Metrics:**
- **Total Tests:** 7
- **Failures:** 7 (100%)
- **Pass Rate:** 0%
- **Execution Time:** 1.87s
- **Platform:** Windows 11 Pro, Python 3.14.3, pytest 9.0.3

---

## Detailed Failure Analysis

### Test 1: `test_api_posts_count_mismatch`
**Status:** ❌ FAILED  
**Error Type:** Assertion Error  
**Failure Message:**
```
AssertionError: Expected 50 posts, got 100
```
**Root Cause:** Hardcoded incorrect count value (50 instead of 100)  
**Correction:** Update expected count from 50 to 100

---

### Test 2: `test_api_invalid_field_name`
**Status:** ❌ FAILED  
**Error Type:** Assertion Error  
**Failure Message:**
```
AssertionError: Post missing key: author
```
**Root Cause:** Incorrect field name in validation - 'author' doesn't exist  
**Correction:** Remove 'author' from required fields

---

### Test 3: `test_api_posts_wrong_range`
**Status:** ❌ FAILED  
**Error Type:** Assertion Error  
**Failure Message:**
```
AssertionError: userId 6 out of expected range 1-5
```
**Root Cause:** Incorrect range validation - expecting 1-5 when actual is 1-10  
**Correction:** Update range from (1, 5) to (1, 10)

---

### Test 4: `test_api_post_body_type_validation`
**Status:** ❌ FAILED  
**Error Type:** Type Validation Error  
**Failure Message:**
```
AssertionError: Post 1 body is type str, expected int but got: quia et suscipit sus...
```
**Root Cause:** Type checking error - expecting int, but API returns string  
**Correction:** Change validation to expect string type

---

### Test 5: `test_api_posts_title_length_check`
**Status:** ❌ FAILED  
**Error Type:** Assertion Error  
**Failure Message:**
```
AssertionError: Post 1 title too short (length: 74), expected >= 100
```
**Root Cause:** Unrealistic title length requirement (100+ characters)  
**Correction:** Remove or adjust title length requirement

---

### Test 6: `test_api_invalid_post_id_format`
**Status:** ❌ FAILED  
**Error Type:** Type Validation Error  
**Failure Message:**
```
AssertionError: Post ID 1 is not a string, got type: int
```
**Root Cause:** Type checking error - expecting str, but API returns int  
**Correction:** Update validation to expect integer type

---

### Test 7: `test_api_user_id_string_validation`
**Status:** ❌ FAILED  
**Error Type:** Type Validation Error  
**Failure Message:**
```
AssertionError: userId 1 is not a numeric string, got type: int
```
**Root Cause:** Type checking error - expecting numeric string, but API returns int  
**Correction:** Update validation to expect integer type

---

## Root Cause Summary

| Category | Count | Percentage |
|----------|-------|-----------|
| Type Validation Errors | 3 | 43% |
| Value Mismatches | 2 | 29% |
| Invalid Field Definitions | 1 | 14% |
| Unrealistic Constraints | 1 | 14% |

---

## Self-Healing Corrections

### Critical Fixes (100% impact)
1. Remove 'author' field validation
2. Fix type checks for body, id, userId fields

### High Priority Fixes
3. Update post count: 50 → 100
4. Update user ID range: (1,5) → (1,10)

### Medium Priority Fixes
5. Remove unrealistic title length constraint

---

*Execution Time: 1.87s | Platform: Python 3.14.3 | Framework: pytest 9.0.3*
