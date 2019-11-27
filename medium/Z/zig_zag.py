class ZigZag:
  def longestZigZag(self, sequence):
    looking_for_high = None
    zig_zag_seq = []
    for i in sequence:
      # if i == 156:
        # breakpoint()
      if zig_zag_seq == []:
        zig_zag_seq.append(i)
      elif zig_zag_seq[-1] < i:
        if looking_for_high or looking_for_high is None:
          zig_zag_seq.append(i)
          looking_for_high = False
        else:
          last = zig_zag_seq.pop(-1)
          zig_zag_seq.append(max(last, i))
      elif zig_zag_seq[-1] > i:
        if looking_for_high is None or not looking_for_high:
          zig_zag_seq.append(i)
          looking_for_high = True
        else:
          last = zig_zag_seq.pop(-1)
          zig_zag_seq.append(min(last, i))

    # print(zig_zag_seq)
    return len(zig_zag_seq)