# Copyright (c) 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

# This file is created by generate_build_files.py. Do not edit manually.

{
  'variables': {
    'boringssl_ssl_sources': [
      '<(openssl_root)/ssl/custom_extensions.c',
      '<(openssl_root)/ssl/d1_both.c',
      '<(openssl_root)/ssl/d1_lib.c',
      '<(openssl_root)/ssl/d1_meth.c',
      '<(openssl_root)/ssl/d1_pkt.c',
      '<(openssl_root)/ssl/d1_srtp.c',
      '<(openssl_root)/ssl/dtls_record.c',
      '<(openssl_root)/ssl/handshake_client.c',
      '<(openssl_root)/ssl/handshake_server.c',
      '<(openssl_root)/ssl/pqueue/pqueue.c',
      '<(openssl_root)/ssl/s3_both.c',
      '<(openssl_root)/ssl/s3_enc.c',
      '<(openssl_root)/ssl/s3_lib.c',
      '<(openssl_root)/ssl/s3_meth.c',
      '<(openssl_root)/ssl/s3_pkt.c',
      '<(openssl_root)/ssl/ssl_aead_ctx.c',
      '<(openssl_root)/ssl/ssl_asn1.c',
      '<(openssl_root)/ssl/ssl_buffer.c',
      '<(openssl_root)/ssl/ssl_cert.c',
      '<(openssl_root)/ssl/ssl_cipher.c',
      '<(openssl_root)/ssl/ssl_ecdh.c',
      '<(openssl_root)/ssl/ssl_file.c',
      '<(openssl_root)/ssl/ssl_lib.c',
      '<(openssl_root)/ssl/ssl_rsa.c',
      '<(openssl_root)/ssl/ssl_session.c',
      '<(openssl_root)/ssl/ssl_stat.c',
      '<(openssl_root)/ssl/t1_enc.c',
      '<(openssl_root)/ssl/t1_lib.c',
      '<(openssl_root)/ssl/tls_record.c',
    ],
    'boringssl_crypto_sources': [
      'err_data.c',
      '<(openssl_root)/crypto/aes/aes.c',
      '<(openssl_root)/crypto/aes/mode_wrappers.c',
      '<(openssl_root)/crypto/asn1/a_bitstr.c',
      '<(openssl_root)/crypto/asn1/a_bool.c',
      '<(openssl_root)/crypto/asn1/a_bytes.c',
      '<(openssl_root)/crypto/asn1/a_d2i_fp.c',
      '<(openssl_root)/crypto/asn1/a_dup.c',
      '<(openssl_root)/crypto/asn1/a_enum.c',
      '<(openssl_root)/crypto/asn1/a_gentm.c',
      '<(openssl_root)/crypto/asn1/a_i2d_fp.c',
      '<(openssl_root)/crypto/asn1/a_int.c',
      '<(openssl_root)/crypto/asn1/a_mbstr.c',
      '<(openssl_root)/crypto/asn1/a_object.c',
      '<(openssl_root)/crypto/asn1/a_octet.c',
      '<(openssl_root)/crypto/asn1/a_print.c',
      '<(openssl_root)/crypto/asn1/a_strnid.c',
      '<(openssl_root)/crypto/asn1/a_time.c',
      '<(openssl_root)/crypto/asn1/a_type.c',
      '<(openssl_root)/crypto/asn1/a_utctm.c',
      '<(openssl_root)/crypto/asn1/a_utf8.c',
      '<(openssl_root)/crypto/asn1/asn1_lib.c',
      '<(openssl_root)/crypto/asn1/asn1_par.c',
      '<(openssl_root)/crypto/asn1/asn_pack.c',
      '<(openssl_root)/crypto/asn1/f_enum.c',
      '<(openssl_root)/crypto/asn1/f_int.c',
      '<(openssl_root)/crypto/asn1/f_string.c',
      '<(openssl_root)/crypto/asn1/t_bitst.c',
      '<(openssl_root)/crypto/asn1/tasn_dec.c',
      '<(openssl_root)/crypto/asn1/tasn_enc.c',
      '<(openssl_root)/crypto/asn1/tasn_fre.c',
      '<(openssl_root)/crypto/asn1/tasn_new.c',
      '<(openssl_root)/crypto/asn1/tasn_typ.c',
      '<(openssl_root)/crypto/asn1/tasn_utl.c',
      '<(openssl_root)/crypto/asn1/x_bignum.c',
      '<(openssl_root)/crypto/asn1/x_long.c',
      '<(openssl_root)/crypto/base64/base64.c',
      '<(openssl_root)/crypto/bio/bio.c',
      '<(openssl_root)/crypto/bio/bio_mem.c',
      '<(openssl_root)/crypto/bio/buffer.c',
      '<(openssl_root)/crypto/bio/connect.c',
      '<(openssl_root)/crypto/bio/fd.c',
      '<(openssl_root)/crypto/bio/file.c',
      '<(openssl_root)/crypto/bio/hexdump.c',
      '<(openssl_root)/crypto/bio/pair.c',
      '<(openssl_root)/crypto/bio/printf.c',
      '<(openssl_root)/crypto/bio/socket.c',
      '<(openssl_root)/crypto/bio/socket_helper.c',
      '<(openssl_root)/crypto/bn/add.c',
      '<(openssl_root)/crypto/bn/asm/x86_64-gcc.c',
      '<(openssl_root)/crypto/bn/bn.c',
      '<(openssl_root)/crypto/bn/bn_asn1.c',
      '<(openssl_root)/crypto/bn/cmp.c',
      '<(openssl_root)/crypto/bn/convert.c',
      '<(openssl_root)/crypto/bn/ctx.c',
      '<(openssl_root)/crypto/bn/div.c',
      '<(openssl_root)/crypto/bn/exponentiation.c',
      '<(openssl_root)/crypto/bn/gcd.c',
      '<(openssl_root)/crypto/bn/generic.c',
      '<(openssl_root)/crypto/bn/kronecker.c',
      '<(openssl_root)/crypto/bn/montgomery.c',
      '<(openssl_root)/crypto/bn/mul.c',
      '<(openssl_root)/crypto/bn/prime.c',
      '<(openssl_root)/crypto/bn/random.c',
      '<(openssl_root)/crypto/bn/rsaz_exp.c',
      '<(openssl_root)/crypto/bn/shift.c',
      '<(openssl_root)/crypto/bn/sqrt.c',
      '<(openssl_root)/crypto/buf/buf.c',
      '<(openssl_root)/crypto/bytestring/asn1_compat.c',
      '<(openssl_root)/crypto/bytestring/ber.c',
      '<(openssl_root)/crypto/bytestring/cbb.c',
      '<(openssl_root)/crypto/bytestring/cbs.c',
      '<(openssl_root)/crypto/chacha/chacha.c',
      '<(openssl_root)/crypto/cipher/aead.c',
      '<(openssl_root)/crypto/cipher/cipher.c',
      '<(openssl_root)/crypto/cipher/derive_key.c',
      '<(openssl_root)/crypto/cipher/e_aes.c',
      '<(openssl_root)/crypto/cipher/e_chacha20poly1305.c',
      '<(openssl_root)/crypto/cipher/e_des.c',
      '<(openssl_root)/crypto/cipher/e_null.c',
      '<(openssl_root)/crypto/cipher/e_rc2.c',
      '<(openssl_root)/crypto/cipher/e_rc4.c',
      '<(openssl_root)/crypto/cipher/e_ssl3.c',
      '<(openssl_root)/crypto/cipher/e_tls.c',
      '<(openssl_root)/crypto/cipher/tls_cbc.c',
      '<(openssl_root)/crypto/cmac/cmac.c',
      '<(openssl_root)/crypto/conf/conf.c',
      '<(openssl_root)/crypto/cpu-aarch64-linux.c',
      '<(openssl_root)/crypto/cpu-arm-linux.c',
      '<(openssl_root)/crypto/cpu-arm.c',
      '<(openssl_root)/crypto/cpu-intel.c',
      '<(openssl_root)/crypto/crypto.c',
      '<(openssl_root)/crypto/curve25519/curve25519.c',
      '<(openssl_root)/crypto/curve25519/spake25519.c',
      '<(openssl_root)/crypto/curve25519/x25519-x86_64.c',
      '<(openssl_root)/crypto/des/des.c',
      '<(openssl_root)/crypto/dh/check.c',
      '<(openssl_root)/crypto/dh/dh.c',
      '<(openssl_root)/crypto/dh/dh_asn1.c',
      '<(openssl_root)/crypto/dh/params.c',
      '<(openssl_root)/crypto/digest/digest.c',
      '<(openssl_root)/crypto/digest/digests.c',
      '<(openssl_root)/crypto/dsa/dsa.c',
      '<(openssl_root)/crypto/dsa/dsa_asn1.c',
      '<(openssl_root)/crypto/ec/ec.c',
      '<(openssl_root)/crypto/ec/ec_asn1.c',
      '<(openssl_root)/crypto/ec/ec_key.c',
      '<(openssl_root)/crypto/ec/ec_montgomery.c',
      '<(openssl_root)/crypto/ec/oct.c',
      '<(openssl_root)/crypto/ec/p224-64.c',
      '<(openssl_root)/crypto/ec/p256-64.c',
      '<(openssl_root)/crypto/ec/p256-x86_64.c',
      '<(openssl_root)/crypto/ec/simple.c',
      '<(openssl_root)/crypto/ec/util-64.c',
      '<(openssl_root)/crypto/ec/wnaf.c',
      '<(openssl_root)/crypto/ecdh/ecdh.c',
      '<(openssl_root)/crypto/ecdsa/ecdsa.c',
      '<(openssl_root)/crypto/ecdsa/ecdsa_asn1.c',
      '<(openssl_root)/crypto/engine/engine.c',
      '<(openssl_root)/crypto/err/err.c',
      '<(openssl_root)/crypto/evp/digestsign.c',
      '<(openssl_root)/crypto/evp/evp.c',
      '<(openssl_root)/crypto/evp/evp_asn1.c',
      '<(openssl_root)/crypto/evp/evp_ctx.c',
      '<(openssl_root)/crypto/evp/p_dsa_asn1.c',
      '<(openssl_root)/crypto/evp/p_ec.c',
      '<(openssl_root)/crypto/evp/p_ec_asn1.c',
      '<(openssl_root)/crypto/evp/p_rsa.c',
      '<(openssl_root)/crypto/evp/p_rsa_asn1.c',
      '<(openssl_root)/crypto/evp/pbkdf.c',
      '<(openssl_root)/crypto/evp/print.c',
      '<(openssl_root)/crypto/evp/sign.c',
      '<(openssl_root)/crypto/ex_data.c',
      '<(openssl_root)/crypto/hkdf/hkdf.c',
      '<(openssl_root)/crypto/hmac/hmac.c',
      '<(openssl_root)/crypto/lhash/lhash.c',
      '<(openssl_root)/crypto/md4/md4.c',
      '<(openssl_root)/crypto/md5/md5.c',
      '<(openssl_root)/crypto/mem.c',
      '<(openssl_root)/crypto/modes/cbc.c',
      '<(openssl_root)/crypto/modes/cfb.c',
      '<(openssl_root)/crypto/modes/ctr.c',
      '<(openssl_root)/crypto/modes/gcm.c',
      '<(openssl_root)/crypto/modes/ofb.c',
      '<(openssl_root)/crypto/newhope/error_correction.c',
      '<(openssl_root)/crypto/newhope/newhope.c',
      '<(openssl_root)/crypto/newhope/ntt.c',
      '<(openssl_root)/crypto/newhope/poly.c',
      '<(openssl_root)/crypto/newhope/precomp.c',
      '<(openssl_root)/crypto/newhope/reduce.c',
      '<(openssl_root)/crypto/obj/obj.c',
      '<(openssl_root)/crypto/obj/obj_xref.c',
      '<(openssl_root)/crypto/pem/pem_all.c',
      '<(openssl_root)/crypto/pem/pem_info.c',
      '<(openssl_root)/crypto/pem/pem_lib.c',
      '<(openssl_root)/crypto/pem/pem_oth.c',
      '<(openssl_root)/crypto/pem/pem_pk8.c',
      '<(openssl_root)/crypto/pem/pem_pkey.c',
      '<(openssl_root)/crypto/pem/pem_x509.c',
      '<(openssl_root)/crypto/pem/pem_xaux.c',
      '<(openssl_root)/crypto/pkcs8/p5_pbe.c',
      '<(openssl_root)/crypto/pkcs8/p5_pbev2.c',
      '<(openssl_root)/crypto/pkcs8/p8_pkey.c',
      '<(openssl_root)/crypto/pkcs8/pkcs8.c',
      '<(openssl_root)/crypto/poly1305/poly1305.c',
      '<(openssl_root)/crypto/poly1305/poly1305_arm.c',
      '<(openssl_root)/crypto/poly1305/poly1305_vec.c',
      '<(openssl_root)/crypto/rand/deterministic.c',
      '<(openssl_root)/crypto/rand/rand.c',
      '<(openssl_root)/crypto/rand/urandom.c',
      '<(openssl_root)/crypto/rand/windows.c',
      '<(openssl_root)/crypto/rc4/rc4.c',
      '<(openssl_root)/crypto/refcount_c11.c',
      '<(openssl_root)/crypto/refcount_lock.c',
      '<(openssl_root)/crypto/rsa/blinding.c',
      '<(openssl_root)/crypto/rsa/padding.c',
      '<(openssl_root)/crypto/rsa/rsa.c',
      '<(openssl_root)/crypto/rsa/rsa_asn1.c',
      '<(openssl_root)/crypto/rsa/rsa_impl.c',
      '<(openssl_root)/crypto/sha/sha1.c',
      '<(openssl_root)/crypto/sha/sha256.c',
      '<(openssl_root)/crypto/sha/sha512.c',
      '<(openssl_root)/crypto/stack/stack.c',
      '<(openssl_root)/crypto/thread.c',
      '<(openssl_root)/crypto/thread_none.c',
      '<(openssl_root)/crypto/thread_pthread.c',
      '<(openssl_root)/crypto/thread_win.c',
      '<(openssl_root)/crypto/time_support.c',
      '<(openssl_root)/crypto/x509/a_digest.c',
      '<(openssl_root)/crypto/x509/a_sign.c',
      '<(openssl_root)/crypto/x509/a_strex.c',
      '<(openssl_root)/crypto/x509/a_verify.c',
      '<(openssl_root)/crypto/x509/algorithm.c',
      '<(openssl_root)/crypto/x509/asn1_gen.c',
      '<(openssl_root)/crypto/x509/by_dir.c',
      '<(openssl_root)/crypto/x509/by_file.c',
      '<(openssl_root)/crypto/x509/i2d_pr.c',
      '<(openssl_root)/crypto/x509/pkcs7.c',
      '<(openssl_root)/crypto/x509/rsa_pss.c',
      '<(openssl_root)/crypto/x509/t_crl.c',
      '<(openssl_root)/crypto/x509/t_req.c',
      '<(openssl_root)/crypto/x509/t_x509.c',
      '<(openssl_root)/crypto/x509/t_x509a.c',
      '<(openssl_root)/crypto/x509/x509.c',
      '<(openssl_root)/crypto/x509/x509_att.c',
      '<(openssl_root)/crypto/x509/x509_cmp.c',
      '<(openssl_root)/crypto/x509/x509_d2.c',
      '<(openssl_root)/crypto/x509/x509_def.c',
      '<(openssl_root)/crypto/x509/x509_ext.c',
      '<(openssl_root)/crypto/x509/x509_lu.c',
      '<(openssl_root)/crypto/x509/x509_obj.c',
      '<(openssl_root)/crypto/x509/x509_r2x.c',
      '<(openssl_root)/crypto/x509/x509_req.c',
      '<(openssl_root)/crypto/x509/x509_set.c',
      '<(openssl_root)/crypto/x509/x509_trs.c',
      '<(openssl_root)/crypto/x509/x509_txt.c',
      '<(openssl_root)/crypto/x509/x509_v3.c',
      '<(openssl_root)/crypto/x509/x509_vfy.c',
      '<(openssl_root)/crypto/x509/x509_vpm.c',
      '<(openssl_root)/crypto/x509/x509cset.c',
      '<(openssl_root)/crypto/x509/x509name.c',
      '<(openssl_root)/crypto/x509/x509rset.c',
      '<(openssl_root)/crypto/x509/x509spki.c',
      '<(openssl_root)/crypto/x509/x509type.c',
      '<(openssl_root)/crypto/x509/x_algor.c',
      '<(openssl_root)/crypto/x509/x_all.c',
      '<(openssl_root)/crypto/x509/x_attrib.c',
      '<(openssl_root)/crypto/x509/x_crl.c',
      '<(openssl_root)/crypto/x509/x_exten.c',
      '<(openssl_root)/crypto/x509/x_info.c',
      '<(openssl_root)/crypto/x509/x_name.c',
      '<(openssl_root)/crypto/x509/x_pkey.c',
      '<(openssl_root)/crypto/x509/x_pubkey.c',
      '<(openssl_root)/crypto/x509/x_req.c',
      '<(openssl_root)/crypto/x509/x_sig.c',
      '<(openssl_root)/crypto/x509/x_spki.c',
      '<(openssl_root)/crypto/x509/x_val.c',
      '<(openssl_root)/crypto/x509/x_x509.c',
      '<(openssl_root)/crypto/x509/x_x509a.c',
      '<(openssl_root)/crypto/x509v3/pcy_cache.c',
      '<(openssl_root)/crypto/x509v3/pcy_data.c',
      '<(openssl_root)/crypto/x509v3/pcy_lib.c',
      '<(openssl_root)/crypto/x509v3/pcy_map.c',
      '<(openssl_root)/crypto/x509v3/pcy_node.c',
      '<(openssl_root)/crypto/x509v3/pcy_tree.c',
      '<(openssl_root)/crypto/x509v3/v3_akey.c',
      '<(openssl_root)/crypto/x509v3/v3_akeya.c',
      '<(openssl_root)/crypto/x509v3/v3_alt.c',
      '<(openssl_root)/crypto/x509v3/v3_bcons.c',
      '<(openssl_root)/crypto/x509v3/v3_bitst.c',
      '<(openssl_root)/crypto/x509v3/v3_conf.c',
      '<(openssl_root)/crypto/x509v3/v3_cpols.c',
      '<(openssl_root)/crypto/x509v3/v3_crld.c',
      '<(openssl_root)/crypto/x509v3/v3_enum.c',
      '<(openssl_root)/crypto/x509v3/v3_extku.c',
      '<(openssl_root)/crypto/x509v3/v3_genn.c',
      '<(openssl_root)/crypto/x509v3/v3_ia5.c',
      '<(openssl_root)/crypto/x509v3/v3_info.c',
      '<(openssl_root)/crypto/x509v3/v3_int.c',
      '<(openssl_root)/crypto/x509v3/v3_lib.c',
      '<(openssl_root)/crypto/x509v3/v3_ncons.c',
      '<(openssl_root)/crypto/x509v3/v3_pci.c',
      '<(openssl_root)/crypto/x509v3/v3_pcia.c',
      '<(openssl_root)/crypto/x509v3/v3_pcons.c',
      '<(openssl_root)/crypto/x509v3/v3_pku.c',
      '<(openssl_root)/crypto/x509v3/v3_pmaps.c',
      '<(openssl_root)/crypto/x509v3/v3_prn.c',
      '<(openssl_root)/crypto/x509v3/v3_purp.c',
      '<(openssl_root)/crypto/x509v3/v3_skey.c',
      '<(openssl_root)/crypto/x509v3/v3_sxnet.c',
      '<(openssl_root)/crypto/x509v3/v3_utl.c',
    ],
    'boringssl_linux_aarch64_sources': [
      'linux-aarch64/crypto/aes/aesv8-armx64.S',
      'linux-aarch64/crypto/bn/armv8-mont.S',
      'linux-aarch64/crypto/chacha/chacha-armv8.S',
      'linux-aarch64/crypto/modes/ghashv8-armx64.S',
      'linux-aarch64/crypto/sha/sha1-armv8.S',
      'linux-aarch64/crypto/sha/sha256-armv8.S',
      'linux-aarch64/crypto/sha/sha512-armv8.S',
    ],
    'boringssl_linux_arm_sources': [
      'linux-arm/crypto/aes/aes-armv4.S',
      'linux-arm/crypto/aes/aesv8-armx32.S',
      'linux-arm/crypto/aes/bsaes-armv7.S',
      'linux-arm/crypto/bn/armv4-mont.S',
      'linux-arm/crypto/chacha/chacha-armv4.S',
      'linux-arm/crypto/modes/ghash-armv4.S',
      'linux-arm/crypto/modes/ghashv8-armx32.S',
      'linux-arm/crypto/sha/sha1-armv4-large.S',
      'linux-arm/crypto/sha/sha256-armv4.S',
      'linux-arm/crypto/sha/sha512-armv4.S',
      '<(openssl_root)/crypto/curve25519/asm/x25519-asm-arm.S',
      '<(openssl_root)/crypto/poly1305/poly1305_arm_asm.S',
    ],
    'boringssl_linux_x86_sources': [
      'linux-x86/crypto/aes/aes-586.S',
      'linux-x86/crypto/aes/aesni-x86.S',
      'linux-x86/crypto/aes/vpaes-x86.S',
      'linux-x86/crypto/bn/bn-586.S',
      'linux-x86/crypto/bn/co-586.S',
      'linux-x86/crypto/bn/x86-mont.S',
      'linux-x86/crypto/chacha/chacha-x86.S',
      'linux-x86/crypto/md5/md5-586.S',
      'linux-x86/crypto/modes/ghash-x86.S',
      'linux-x86/crypto/rc4/rc4-586.S',
      'linux-x86/crypto/sha/sha1-586.S',
      'linux-x86/crypto/sha/sha256-586.S',
      'linux-x86/crypto/sha/sha512-586.S',
    ],
    'boringssl_linux_x86_64_sources': [
      'linux-x86_64/crypto/aes/aes-x86_64.S',
      'linux-x86_64/crypto/aes/aesni-x86_64.S',
      'linux-x86_64/crypto/aes/bsaes-x86_64.S',
      'linux-x86_64/crypto/aes/vpaes-x86_64.S',
      'linux-x86_64/crypto/bn/rsaz-avx2.S',
      'linux-x86_64/crypto/bn/rsaz-x86_64.S',
      'linux-x86_64/crypto/bn/x86_64-mont.S',
      'linux-x86_64/crypto/bn/x86_64-mont5.S',
      'linux-x86_64/crypto/chacha/chacha-x86_64.S',
      'linux-x86_64/crypto/ec/p256-x86_64-asm.S',
      'linux-x86_64/crypto/md5/md5-x86_64.S',
      'linux-x86_64/crypto/modes/aesni-gcm-x86_64.S',
      'linux-x86_64/crypto/modes/ghash-x86_64.S',
      'linux-x86_64/crypto/rand/rdrand-x86_64.S',
      'linux-x86_64/crypto/rc4/rc4-x86_64.S',
      'linux-x86_64/crypto/sha/sha1-x86_64.S',
      'linux-x86_64/crypto/sha/sha256-x86_64.S',
      'linux-x86_64/crypto/sha/sha512-x86_64.S',
      '<(openssl_root)/crypto/curve25519/asm/x25519-asm-x86_64.S',
    ],
    'boringssl_mac_x86_sources': [
      'mac-x86/crypto/aes/aes-586.S',
      'mac-x86/crypto/aes/aesni-x86.S',
      'mac-x86/crypto/aes/vpaes-x86.S',
      'mac-x86/crypto/bn/bn-586.S',
      'mac-x86/crypto/bn/co-586.S',
      'mac-x86/crypto/bn/x86-mont.S',
      'mac-x86/crypto/chacha/chacha-x86.S',
      'mac-x86/crypto/md5/md5-586.S',
      'mac-x86/crypto/modes/ghash-x86.S',
      'mac-x86/crypto/rc4/rc4-586.S',
      'mac-x86/crypto/sha/sha1-586.S',
      'mac-x86/crypto/sha/sha256-586.S',
      'mac-x86/crypto/sha/sha512-586.S',
    ],
    'boringssl_mac_x86_64_sources': [
      'mac-x86_64/crypto/aes/aes-x86_64.S',
      'mac-x86_64/crypto/aes/aesni-x86_64.S',
      'mac-x86_64/crypto/aes/bsaes-x86_64.S',
      'mac-x86_64/crypto/aes/vpaes-x86_64.S',
      'mac-x86_64/crypto/bn/rsaz-avx2.S',
      'mac-x86_64/crypto/bn/rsaz-x86_64.S',
      'mac-x86_64/crypto/bn/x86_64-mont.S',
      'mac-x86_64/crypto/bn/x86_64-mont5.S',
      'mac-x86_64/crypto/chacha/chacha-x86_64.S',
      'mac-x86_64/crypto/ec/p256-x86_64-asm.S',
      'mac-x86_64/crypto/md5/md5-x86_64.S',
      'mac-x86_64/crypto/modes/aesni-gcm-x86_64.S',
      'mac-x86_64/crypto/modes/ghash-x86_64.S',
      'mac-x86_64/crypto/rand/rdrand-x86_64.S',
      'mac-x86_64/crypto/rc4/rc4-x86_64.S',
      'mac-x86_64/crypto/sha/sha1-x86_64.S',
      'mac-x86_64/crypto/sha/sha256-x86_64.S',
      'mac-x86_64/crypto/sha/sha512-x86_64.S',
      '<(openssl_root)/crypto/curve25519/asm/x25519-asm-x86_64.S',
    ],
    'boringssl_win_x86_sources': [
      'win-x86/crypto/aes/aes-586.asm',
      'win-x86/crypto/aes/aesni-x86.asm',
      'win-x86/crypto/aes/vpaes-x86.asm',
      'win-x86/crypto/bn/bn-586.asm',
      'win-x86/crypto/bn/co-586.asm',
      'win-x86/crypto/bn/x86-mont.asm',
      'win-x86/crypto/chacha/chacha-x86.asm',
      'win-x86/crypto/md5/md5-586.asm',
      'win-x86/crypto/modes/ghash-x86.asm',
      'win-x86/crypto/rc4/rc4-586.asm',
      'win-x86/crypto/sha/sha1-586.asm',
      'win-x86/crypto/sha/sha256-586.asm',
      'win-x86/crypto/sha/sha512-586.asm',
    ],
    'boringssl_win_x86_64_sources': [
      'win-x86_64/crypto/aes/aes-x86_64.asm',
      'win-x86_64/crypto/aes/aesni-x86_64.asm',
      'win-x86_64/crypto/aes/bsaes-x86_64.asm',
      'win-x86_64/crypto/aes/vpaes-x86_64.asm',
      'win-x86_64/crypto/bn/rsaz-avx2.asm',
      'win-x86_64/crypto/bn/rsaz-x86_64.asm',
      'win-x86_64/crypto/bn/x86_64-mont.asm',
      'win-x86_64/crypto/bn/x86_64-mont5.asm',
      'win-x86_64/crypto/chacha/chacha-x86_64.asm',
      'win-x86_64/crypto/ec/p256-x86_64-asm.asm',
      'win-x86_64/crypto/md5/md5-x86_64.asm',
      'win-x86_64/crypto/modes/aesni-gcm-x86_64.asm',
      'win-x86_64/crypto/modes/ghash-x86_64.asm',
      'win-x86_64/crypto/rand/rdrand-x86_64.asm',
      'win-x86_64/crypto/rc4/rc4-x86_64.asm',
      'win-x86_64/crypto/sha/sha1-x86_64.asm',
      'win-x86_64/crypto/sha/sha256-x86_64.asm',
      'win-x86_64/crypto/sha/sha512-x86_64.asm',
    ],
  }
}
