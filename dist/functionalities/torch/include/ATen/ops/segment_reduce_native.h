#pragma once

// @generated by torchgen/gen.py from NativeFunction.h

#include <c10/core/Scalar.h>
#include <c10/core/Storage.h>
#include <c10/core/TensorOptions.h>
#include <c10/util/Deprecated.h>
#include <c10/util/Optional.h>
#include <c10/core/QScheme.h>
#include <ATen/core/Reduction.h>
#include <ATen/core/Tensor.h>
#include <tuple>
#include <vector>


namespace at {
namespace native {
TORCH_API at::Tensor & segment_reduce_out(const at::Tensor & data, c10::string_view reduce, const c10::optional<at::Tensor> & lengths, const c10::optional<at::Tensor> & indices, const c10::optional<at::Tensor> & offsets, int64_t axis, bool unsafe, const c10::optional<at::Scalar> & initial, at::Tensor & out);
TORCH_API at::Tensor segment_reduce_kernel(const at::Tensor & data, c10::string_view reduce, const c10::optional<at::Tensor> & lengths={}, const c10::optional<at::Tensor> & indices={}, const c10::optional<at::Tensor> & offsets={}, int64_t axis=0, bool unsafe=false, const c10::optional<at::Scalar> & initial=c10::nullopt);
} // namespace native
} // namespace at
