require_relative './test_helper'

describe 'string conversions' do
  it 'converts strings safely to query format and back' do
    strings = [
      'simple-string',
      'complex.string/with-123',
      'numbers-0123456789',
      'symbols-and-digits-9/8.7'
    ]

    strings.each do |original|
      safe = convert_from_real_to_query_safe(original)
      back = convert_from_query_safe_to_real(safe)
      _(back).must_equal original
    end
  end
end
