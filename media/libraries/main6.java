public static String generateBase32Secret(int numDigits) {
		StringBuilder sb = new StringBuilder(numDigits);
		Random random = new SecureRandom();
		for (int i = 0; i < numDigits; i++) {
			int val = random.nextInt(32);
			if (val < 26) {
				sb.append((char) ('A' + val));
			} else {
				sb.append((char) ('2' + (val - 26)));
			}
		}
		return sb.toString();
	}


    	/**
	 * Similar to {@link #generateHexSecret()} but specifies a character length.
	 */
	public static String generateHexSecret(int numDigits) {
		StringBuilder sb = new StringBuilder(numDigits);
		Random random = new SecureRandom();
		for (int i = 0; i < numDigits; i++) {
			int val = random.nextInt(16);
			if (val < 10) {
				sb.append((char) ('0' + val));
			} else {
				sb.append((char) ('A' + (val - 10)));
			}
		}
		return sb.toString();
	}
